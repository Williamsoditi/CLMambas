from rest_framework import generics
from .models import Schedule, League
from .serializers import GameSerializer, LeagueSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

# Create your views here.
class GameList(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Schedule.objects.select_related('league').all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return  [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]
    

class GameRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Schedule.objects.select_related('league').all()

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'PATCH']:
            return  [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]    


class LeagueList(generics.ListCreateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    permission_classes = [IsAdminUser]

class LeagueRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer
    permission_classes = [IsAdminUser]