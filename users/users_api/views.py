from users_api.serializers import UserSerializer, UserPasswordSerializer
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User

# Create your views here.


class UserViewSet(viewsets.ViewSet):
    def create(self, request):
        print(request.data)
        serializer = UserPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print("success")
        return Response(status=status.HTTP_201_CREATED)

    def authenticateGetId(self, request):
        data = request.data
        username = data["username"]
        password = data["password"]
        print(User.objects.all())
        userExists = User.objects.filter(
            username=username, password=password).exists()
        if not userExists:
            return Response(status=status.HTTP_204_NO_CONTENT)

        user = User.objects.get(username=username, password=password)

        return Response(user.id, status=status.HTTP_200_OK)

    def getUsername(self, request, pk=None):
        user = User.objects.get(id=pk)
        return Response(user.username, status=status.HTTP_200_OK)
