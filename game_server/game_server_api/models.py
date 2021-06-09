from django.db import models
from datetime import datetime
from django.db.models.constraints import UniqueConstraint

from django.db.models.deletion import CASCADE

# Create your models here.


class Game(models.Model):  # id lobby to id w bazie danych
    round_start = models.DateTimeField(
        default=datetime(1970, 1, 1)
    )
    game_started = models.BooleanField(
        default=False
    )
    round_no = models.IntegerField(
        default=0
    )
    round_ended = models.BooleanField(
        default=False
    )
    title_weight = models.FloatField(
        default=0.5
    )
    author_weight = models.FloatField(
        default=0.5
    )
    source_weight = models.FloatField(
        default=0
    )
    game_ended = models.BooleanField(
        default=False
    )


class Song(models.Model):
    url = models.URLField(
        max_length=128
    )
    title = models.CharField(
        max_length=128
    )
    author = models.CharField(
        max_length=128
    )
    source = models.CharField(
        max_length=128
    )
    game_id = models.ForeignKey(
        Game,
        on_delete=CASCADE
    )
    round_no = models.IntegerField(
        default=1
    )


class Player(models.Model):
    player_id = models.IntegerField(
        default=0
    )
    score = models.FloatField(
        default=0
    )
    last_title = models.CharField(
        max_length=128,
        default=''
    )
    last_author = models.CharField(
        max_length=128,
        default=''
    )
    last_source = models.CharField(
        max_length=128,
        default=''
    )
    correct_title = models.BooleanField(
        default=False
    )
    correct_author = models.BooleanField(
        default=False
    )
    correct_source = models.BooleanField(
        default=False
    )
    game_id = models.ForeignKey(
        Game,
        on_delete=CASCADE
    )
    round_no = models.IntegerField(
        default=0
    )

    class Meta:
        constraints = [
            UniqueConstraint(fields=['player_id', 'game_id'],
                             name='player_once_in_game')
        ]
