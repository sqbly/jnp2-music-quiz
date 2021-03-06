from game_server_api.serializers import SongSerializer, PlayerSerializer, PlayerScoreSerializer, GameSerializer
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
import requests
from datetime import datetime, timezone
from .models import Game, Song, Player
import celery

ROUNDS_IN_GAME = 4

# Create your views here.


class GameViewSet(viewsets.ViewSet):
    def createLobby(self, request):
        serializer = GameSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        game = serializer.save()

        for i in range(ROUNDS_IN_GAME):
            songRequest = requests.get(
                'http://10.64.0.130:8000/api/songs/random')

            song_serializer = SongSerializer(data=songRequest.json())
            song_serializer.is_valid(raise_exception=True)
            song = song_serializer.save(game_id=game, round_no=i+1)
            print(song.title)

        player = Player(player_id=request.data['player_id'], game_id=game)
        player.save()

        return Response(game.id, status=status.HTTP_201_CREATED)

    def joinLobby(self, request, pk=None):
        game = Game.objects.get(id=pk)

        player = Player(player_id=request.data['player_id'], game_id=game)
        player.save()

        return Response(status=status.HTTP_200_OK)

    def startGame(self, request, pk=None):
        game = Game.objects.get(id=pk)

        player_id = request.data['player_id']

        if not Player.objects.filter(player_id=player_id, game_id=game).exists():
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        game.game_started = True

        game.save()

        print(Game.objects.all())

        return Response(status=status.HTTP_200_OK)

    def getGameState(self, request, pk=None):
        game = Game.objects.get(id=pk)

        # update round state

        if not game.game_started:
            players = list(Player.objects.filter(game_id=game))
            print(players)
            players_data = [PlayerSerializer(
                p).data for p in players]

            return Response({'game_state': 'waiting_for_players', 'players': players_data}, status=status.HTTP_200_OK)

        if (datetime.now(timezone.utc) - game.round_start).total_seconds() > 25:
            game.round_no = game.round_no+1
            game.round_ended = False
            game.round_start = datetime.now(timezone.utc)

        if (datetime.now(timezone.utc) - game.round_start).total_seconds() > 20:
            game.round_ended = True

        game.save()

        if game.round_no > ROUNDS_IN_GAME:
            if (not game.game_ended):
                players = list(Player.objects.filter(game_id=game))
                for player in players:
                    celery.current_app.send_task('stats_api.tasks.consume', [{
                                                 'player_id': player.player_id, 'score': player.score, 'game_id': game.id}])
            game.game_ended = True
            game.save()

        if game.game_ended:
            players = list(Player.objects.filter(game_id=game))
            print(players)
            players_data = [PlayerScoreSerializer(
                p).data for p in players]

            return Response({'game_state': 'game_ended',  'players': players_data}, status=status.HTTP_200_OK)

        print("ROUND NO")
        print(game.round_no)

        if game.round_ended:
            # round ended
            players = list(Player.objects.filter(game_id=game))
            print(players)
            players_data = [PlayerSerializer(
                p).data for p in players]

            return Response({'round': game.round_no, 'game_state': 'round_ended', 'players': players_data}, status=status.HTTP_200_OK)
        else:
            song = Song.objects.get(game_id=game, round_no=game.round_no)
            return Response({'round': game.round_no, 'game_state': 'guessing_time', 'url': song.url, 'round': game.round_no}, status=status.HTTP_200_OK)

    def receiveAnswer(self, request, pk=None):
        game = Game.objects.get(id=pk)

        if game.round_ended:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        answer_round = int(request.data['round'])
        answer_title = request.data['title'].strip().lower()
        answer_author = request.data['author'].strip().lower()
        answer_source = request.data['source'].strip().lower()
        player_id = request.data['player_id']

        player = Player.objects.get(
            player_id=player_id, game_id=game)  # will throw 500 welp

        if player.round_no >= answer_round or game.round_no > answer_round:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        song = Song.objects.get(game_id=game, round_no=answer_round)

        if answer_title == song.title.strip().lower():
            player.score = player.score + game.title_weight
            player.correct_title = True
        else:
            player.correct_title = False

        if answer_author == song.author.strip().lower():
            player.score = player.score + game.author_weight
            player.correct_author = True
        else:
            player.correct_author = False

        if answer_source == song.source.strip().lower():
            player.score = player.score + game.source_weight
            player.correct_source = True
        else:
            player.correct_source = False

        print(player.score)

        player.round_no = game.round_no

        player.last_title = answer_title
        player.last_author = answer_author
        player.last_source = answer_source

        player.save()

        return Response(status=status.HTTP_200_OK)
