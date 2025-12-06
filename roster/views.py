from django.shortcuts import render
from rest_framework import generics
from .models import Player
from .serializers import PlayerSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

# Create your views here.
class PlayerList(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method == 'POST':
            return  [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

class PlayerDetail(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer 
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'PATCH']:
            return  [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]
