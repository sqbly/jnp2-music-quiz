from django.urls import path

from .views import UserViewSet

urlpatterns = [
    path('users', UserViewSet.as_view({
        'post': 'create'
    })),
    path('users/login', UserViewSet.as_view({
        'post': 'authenticateGetId'
    })),
    path('users/<str:pk>', UserViewSet.as_view({
        'get': 'getUsername'
    }))
]
