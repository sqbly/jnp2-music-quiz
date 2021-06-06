from django.urls import path

from .views import GameViewSet

urlpatterns = [
    path('game_server', GameViewSet.as_view({
        'post': 'createLobby'
    })),
    path('game_server/join/<str:pk>', GameViewSet.as_view({
        'post': 'joinLobby'
    })),
    path('game_server/start/<str:pk>', GameViewSet.as_view({
        'post': 'startGame'
    })),
    path('game_server/<str:pk>', GameViewSet.as_view({
        'get': 'getGameState',
        'post': 'receiveAnswer'
    }))
]
