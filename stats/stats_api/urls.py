from django.urls import path

from .views import StatsViewSet

urlpatterns = [
    path('user/<str:pk>', StatsViewSet.as_view({
        'get': 'getStatsForPlayer'
    }))
]
