from django.urls import path
from .views import *


urlpatterns = [
    path('schedule/', GameList.as_view(), name='game-list'),
    path('schedule/<int:pk>/', GameRetrieve.as_view(), name='game-detail'),
    path('leagues/', LeagueList.as_view(), name='league-list-create'),
    path('leagues/<int:pk>/', LeagueRetrieve.as_view(), name='league-detail-update-destroy'),
]