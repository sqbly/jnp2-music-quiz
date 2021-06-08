# Generated by Django 3.2.4 on 2021-06-05 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=128, unique=True)),
                ('title', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=128)),
                ('source', models.CharField(max_length=128)),
            ],
        ),
    ]
