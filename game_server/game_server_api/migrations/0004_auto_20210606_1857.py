# Generated by Django 3.2.4 on 2021-06-06 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_server_api', '0003_alter_player_last_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='last_answer',
            new_name='last_author',
        ),
        migrations.AddField(
            model_name='player',
            name='last_source',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='player',
            name='last_title',
            field=models.CharField(default='', max_length=128),
        ),
    ]
