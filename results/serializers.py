# results_app/serializers.py
from rest_framework import serializers
from .models import GameResult

class GameResultSerializer(serializers.ModelSerializer):
    recorded_at = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", read_only=True)
    last_updated = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", read_only=True)

    # Fields to display team names and scores dynamically
    home_team_name = serializers.SerializerMethodField()
    away_team_name = serializers.SerializerMethodField()
    
    league_name = serializers.SerializerMethodField()

    class Meta:
        model = GameResult
        fields = (
            'id',
            'home_team_name',
            'home_score',  
            'away_team_name',
            'away_score', 
            'status',
            'recorded_at',
            'last_updated',
        )
        read_only_fields = ['recorded_at', 'last_updated']
        
    def get_league_name(self, obj):
        return obj.schedule.league.name if obj.schedule.league else "N/A League"

    

    def get_home_team_name(self, obj):
        schedule = obj.schedule
        # Determine which team is the true 'home' team for this specific game
        if schedule.game_type == 'HOME':
            # If 'Clique Mambas' is the home team for this schedule entry
            return "Clique Mambas"
        else:
            # If the opponent is the home team for this schedule entry
            return schedule.opponent

    def get_away_team_name(self, obj):
        schedule = obj.schedule
        # Determine which team is the true 'away' team for this specific game
        if schedule.game_type == 'AWAY':
            # If 'Clique Mambas' is the away team for this schedule entry
            return "Clique Mambas"
        else:
            # If the opponent is the away team for this schedule entry
            return schedule.opponent