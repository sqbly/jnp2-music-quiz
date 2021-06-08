from django.http.response import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.template import loader
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import HttpResponse
import requests
from .forms import LoginForm, RegistrationForm, LobbyCreationForm

# Create your views here.


class LoginLogoutViewSet(viewsets.ViewSet):
    def loginService(self, request):
        form = LoginForm(request.POST)

        if not form.is_valid():
            return HttpResponseBadRequest()

        url = 'http://host.docker.internal:8001/api/users/login'

        data = {'username': form.cleaned_data['login'],
                'password': form.cleaned_data['password']}

        userRequest = requests.post(url, data=data)

        print(userRequest.status_code)
        print(userRequest.content)

        if userRequest.status_code == 200:
            request.session['player_id'] = int(userRequest.content)
            return redirect('/')

        return redirect('/login')

    def loginPage(self, request):
        if 'player_id' in request.session:
            return redirect('/')
        template = loader.get_template('front_server/login_page.html')
        context = {'form': LoginForm()}
        return HttpResponse(template.render(context, request))

    def logout(self, request):
        if 'player_id' in request.session:
            del request.session['player_id']
        return redirect('/login')

    def userCreationPage(self, request):
        if 'player_id' in request.session:
            return redirect('/')
        template = loader.get_template('front_server/registration_page.html')
        context = {'form': RegistrationForm()}
        return HttpResponse(template.render(context, request))

    def createUser(self, request):
        form = RegistrationForm(request.POST)

        if not form.is_valid():
            return HttpResponseBadRequest()

        url = 'http://host.docker.internal:8001/api/users'

        data = {'username': form.cleaned_data['login'],
                'password': form.cleaned_data['password']}

        userRequest = requests.post(url, data=data)

        print(userRequest.status_code)
        print(userRequest.content)

        if userRequest.status_code == 500:
            template = loader.get_template(
                'front_server/registration_page.html')
            context = {'form': RegistrationForm(), 'failed': True}
            return HttpResponse(template.render(context, request))

        return redirect('/login')


class HomeViewSet(viewsets.ViewSet):
    def homePage(self, request):
        if 'player_id' not in request.session:
            return redirect('/login')

        template = loader.get_template('front_server/index.html')
        context = {}
        return HttpResponse(template.render(context, request))

    def statsPage(self, request):
        return redirect('/')


class GameViewSet(viewsets.ViewSet):
    def lobbyCreationPage(self, request):
        if 'player_id' not in request.session:
            return redirect('/login')

        template = loader.get_template('front_server/lobby_creation_page.html')
        context = {'form': LobbyCreationForm()}
        return HttpResponse(template.render(context, request))

    def createLobby(self, request):
        if 'player_id' not in request.session:
            return redirect('/login')

        form = LobbyCreationForm(request.POST)

        if not form.is_valid():
            return HttpResponseBadRequest()

        url = 'http://host.docker.internal:8002/api/game_server'

        data = {'title_weight': form.cleaned_data['titleWeight'],
                'author_weight': form.cleaned_data['authorWeight'],
                'source_weight': form.cleaned_data['sourceWeight'],
                'player_id': request.session['player_id']}

        lobbyCreateRequest = requests.post(url, data=data)

        print(lobbyCreateRequest.status_code)
        print(lobbyCreateRequest.content)

        if lobbyCreateRequest.status_code == 201:
            lobbyId = int(lobbyCreateRequest.content)
            return redirect('/lobby/' + str(lobbyId))

        return redirect('/create')

    def startLobby(self, request, nr=None):
        if 'player_id' not in request.session:
            return redirect('/login')

        url = 'http://host.docker.internal:8002/api/game_server/start/' + \
            str(nr)

        data = {'player_id': request.session['player_id']}

        lobbyStartRequest = requests.post(url, data=data)

        return Response(status=lobbyStartRequest.status_code)

    def lobbyPage(self, request, nr=None):
        if 'player_id' not in request.session:
            return redirect('/login')

        template = loader.get_template('front_server/lobby.html')
        context = {'lobbyId': nr}
        return HttpResponse(template.render(context, request))

    def joinLobby(self, request, nr=None):
        if 'player_id' not in request.session:
            return redirect('/login')

        url = 'http://host.docker.internal:8002/api/game_server/join/' + \
            str(nr)

        data = {'player_id': request.session['player_id']}

        joinLobbyRequest = requests.post(url, data=data)

        if joinLobbyRequest.status_code == 200:
            return redirect('/lobby/' + str(nr))

        return redirect('')

    def getGameState(self, request, nr=None):
        if 'player_id' not in request.session:
            return redirect('/login')

        url = 'http://host.docker.internal:8002/api/game_server/' + str(nr)

        data = {}

        gameStateRequest = requests.get(url, data=data)

        print(gameStateRequest.json())

        return Response(status=gameStateRequest.status_code, data=gameStateRequest.json())

    def postAnswer(self, request, nr=None):
        if 'player_id' not in request.session:
            return redirect('/login')

        url = 'http://host.docker.internal:8002/api/game_server/' + str(nr)

        data = {'player_id': request.session['player_id'],
                'round': request.data['round'],
                'title': request.data['title'],
                'author': request.data['author'],
                'source': request.data['source']}

        answerRequest = requests.post(url, data=data)

        return Response(status=answerRequest.status_code)


class SongsViewSet(viewsets.ViewSet):

    def songsPage(self, request):
        pass

    def uploadSong(self, request):
        pass

    def deleteSong(self, request):
        pass
