# results_app/views.py
from rest_framework import viewsets
from .models import GameResult
from .serializers import GameResultSerializer

class GameResultViewSet(viewsets.ModelViewSet):
    queryset = GameResult.objects.all().order_by('-schedule__game_date', '-recorded_at')
    serializer_class = GameResultSerializer