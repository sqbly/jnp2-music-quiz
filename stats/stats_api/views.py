from rest_framework import viewsets, status
from rest_framework.response import Response
from stats_api.serializers import RecordedGameSerializer
from .models import RecordedGame
from django.db.models import Sum, Count

# Create your views here.


class StatsViewSet(viewsets.ViewSet):
    def getStatsForPlayer(self, request, pk=None):
        games = RecordedGame.objects.filter(player_id=pk).aggregate(
            Sum('score'), Count('game_id'))

        print(games)

        return Response(games, status=status.HTTP_200_OK)
