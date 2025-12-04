from django.shortcuts import render
from rest_framework import generics
from .models import Schedule
from .serializers import GameSerializer

# Create your views here.
class GameList(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveAPIView):
    queryset = Schedule.objects.all()
    serializer_class = GameSerializer
