# Generated by Django 3.2.4 on 2021-06-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_server_api', '0008_game_game_ended'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='correct_author',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='correct_source',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='correct_title',
            field=models.BooleanField(default=False),
        ),
    ]
