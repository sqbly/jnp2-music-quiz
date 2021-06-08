from django.urls import path

from .views import LoginLogoutViewSet, HomeViewSet, GameViewSet, SongsViewSet

urlpatterns = [
    path('', HomeViewSet.as_view({
        'get': 'homePage'
    })),
    path('login', LoginLogoutViewSet.as_view({
        'get': 'loginPage',
        'post': 'loginService'
    })),
    path('logout', LoginLogoutViewSet.as_view({
        'get': 'logout'
    })),
    path('register', LoginLogoutViewSet.as_view({
        'get': 'userCreationPage',
        'post': 'createUser'
    })),
    path('stats', HomeViewSet.as_view({
        'get': 'statsPage'
    })),
    path('create', GameViewSet.as_view({
        'get': 'lobbyCreationPage',
        'post': 'createLobby'
    })),
    path('lobby/<str:nr>', GameViewSet.as_view({
        'get': 'lobbyPage'
    })),
    path('lobby/<str:nr>/answer', GameViewSet.as_view({
        'post': 'postAnswer'
    })),
    path('lobby/<str:nr>/info', GameViewSet.as_view({
        'get': 'getGameInfo'
    })),
    path('songs', SongsViewSet.as_view({
        'get': 'songsPage',
        'post': 'uploadSong',
        'delete': 'deleteSong'
    }))
]
