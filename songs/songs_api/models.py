from django.db import models
from django.db.models.constraints import UniqueConstraint

# Create your models here.


class Song(models.Model):
    url = models.URLField(
        max_length=128,
        unique=True
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
    start_point = models.IntegerField(
        default=0
    )
    length = models.PositiveIntegerField(
        default=90
    )

    UniqueConstraint(fields=['title', 'author', 'source'], name='unique_songs')
