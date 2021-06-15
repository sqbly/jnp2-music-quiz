from django.db import models
from django.db.models.constraints import UniqueConstraint

# Create your models here.


class RecordedGame(models.Model):
    player_id = models.IntegerField(
        default=0
    )
    score = models.FloatField(
        default=0
    )
    game_id = models.IntegerField(
        default=0
    )

    class Meta:
        constraints = [
            UniqueConstraint(fields=['player_id', 'game_id'],
                             name='player_once_in_game')
        ]
