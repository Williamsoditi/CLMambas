from django.shortcuts import render
from rest_framework import generics
from .models import Player
from .serializers import PlayerSerializer

# Create your views here.
class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'PATCH']:
            return  [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'PATCH']:
            return  [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]
