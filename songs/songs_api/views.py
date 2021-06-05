from songs_api.serializers import SongSerializer
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Song

import random

# Create your views here.


class SongViewSet(viewsets.ViewSet):
    def retrieveRandom(self, request):
        songs = Song.objects.all()
        song = random.choice(songs)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def create(self, request):  # jak do penisa to ma działać??
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
        song = Song.objects.get(id=pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieveAll(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
