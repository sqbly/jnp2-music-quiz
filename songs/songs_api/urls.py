from django.urls import path

from .views import SongViewSet

urlpatterns = [
    path('songs', SongViewSet.as_view({
        'get': 'retrieveAll',
        'post': 'create'
    })),
    path('songs/random', SongViewSet.as_view({
        'get': 'retrieveRandom'
    })),
    path('songs/<str:pk>', SongViewSet.as_view({
        'delete': 'destroy'
    }))
]
