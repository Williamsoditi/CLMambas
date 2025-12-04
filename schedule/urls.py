from django.urls import path
from .views import GameList, GameDetail

urlpatterns = [
    path('schedule/', GameList.as_view(), name='game-list'),
    path('schedule/<int:pk>/', GameDetail.as_view(), name='game-detail'),
]