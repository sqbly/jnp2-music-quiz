from songs_api.serializers import SongSerializer
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Song

import random

# Create your views here.


def songPrepper(url):
    url = url.replace('watch?v=', 'embed/')
    url = url + '?autoplay=1'
    return url


class SongViewSet(viewsets.ViewSet):
    def retrieveRandom(self, request):
        songs = Song.objects.all()
        song = random.choice(songs)
        serializer = SongSerializer(song)
        data = serializer.data
        data['url'] = data['url'] + '&start=' + str(random.randint(
            data['start_point'], data['length'] - 20))
        return Response(data)

    def create(self, request):
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['url'] = songPrepper(
            serializer.validated_data['url'])
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
