from rest_framework import serializers

from .models import RecordedGame


class RecordedGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordedGame
        fields = ['player_id', 'score', 'game_id']
