# Generated by Django 3.2.4 on 2021-06-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_server_api', '0009_auto_20210608_1516'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='player',
            constraint=models.UniqueConstraint(fields=('player_id', 'game_id'), name='player_once_in_game'),
        ),
    ]
