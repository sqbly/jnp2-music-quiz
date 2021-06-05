from django.db import models
from django.db.models.constraints import UniqueConstraint


# Create your models here.

class User(models.Model):
    username = models.CharField(
        max_length=64,
        unique=True
    )
    password = models.CharField(
        max_length=64
    )
    is_superuser = models.BooleanField(
        default=False
    )
