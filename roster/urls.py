from django.urls import path
from .views import PlayerList, PlayerDetail

urlpatterns = [
    path('roster/', PlayerList.as_view(), name='player-list'),
    path('roster/<int:pk>/', PlayerDetail.as_view(), name='player-detail'),
]