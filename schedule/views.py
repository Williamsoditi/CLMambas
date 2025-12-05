from rest_framework import generics
from .models import Schedule
from .serializers import GameSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

# Create your views here.
class GameList(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method = 'POST':
            return  [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

class GameDetail(generics.RetrieveAPIView):
    queryset = Schedule.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'PATCH']:
            return  [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]    
