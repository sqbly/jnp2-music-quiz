# Generated by Django 3.2.4 on 2021-06-15 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecordedGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0)),
                ('game_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddConstraint(
            model_name='recordedgame',
            constraint=models.UniqueConstraint(fields=('player_id', 'game_id'), name='player_once_in_game'),
        ),
    ]
