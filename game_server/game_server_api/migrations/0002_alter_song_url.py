# Generated by Django 3.2.4 on 2021-06-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_server_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='url',
            field=models.URLField(max_length=128),
        ),
    ]
