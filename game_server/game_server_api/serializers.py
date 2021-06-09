from rest_framework import serializers

from .models import Song, Player, Game


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['url', 'title', 'author', 'source']


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player_id', 'last_title', 'last_author', 'last_source',
                  'correct_title', 'correct_author', 'correct_source', 'round_no']


class PlayerScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player_id', 'score']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['title_weight', 'author_weight', 'source_weight']
