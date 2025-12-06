from rest_framework import serializers
from .models import GameResult

class GameResultSerializer(serializers.ModelSerializer):
    recorded_at = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", read_only=True)
    last_updated = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", read_only=True)
    
    class Meta:
        model = GameResult
        fields = 'id', 'home_score', 'away_score', 'status', 'recorded_at', 'last_updated'
        read_only_fields = ['recorded_at', 'last_updated']