from django.http.response import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.template import loader
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import HttpResponse
import requests
from .forms import LoginForm, RegistrationForm

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
            request.session['user_id'] = int(userRequest.content)
            return redirect('/')

        return redirect('/login')

    def loginPage(self, request):
        if 'user_id' in request.session:
            return redirect('/')
        template = loader.get_template('front_server/login_page.html')
        context = {'form': LoginForm()}
        return HttpResponse(template.render(context, request))

    def logout(self, request):
        if 'user_id' in request.session:
            del request.session['user_id']
        return redirect('/login')

    def userCreationPage(self, request):
        if 'user_id' in request.session:
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
        if 'user_id' not in request.session:
            return redirect('/login')

        template = loader.get_template('front_server/index.html')
        context = {}
        return HttpResponse(template.render(context, request))

    def statsPage(self, request):
        return redirect('/')


class GameViewSet(viewsets.ViewSet):
    def lobbyCreationPage(self, request):
        if 'user_id' not in request.session:
            return redirect('/login')

    def createLobby(self, request):
        pass

    def lobbyPage(self, request):
        pass

    def getGameInfo(self, request):
        pass

    def postAnswer(self, request):
        pass


class SongsViewSet(viewsets.ViewSet):

    def songsPage(self, request):
        pass

    def uploadSong(self, request):
        pass

    def deleteSong(self, request):
        pass
