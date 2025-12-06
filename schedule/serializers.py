import datetime
from rest_framework import serializers
from .models import League, Schedule
from results.models import GameResult


# Serializer for the League model
class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'

# Serializer for the Schedule model
class GameSerializer(serializers.ModelSerializer):
    league_name = serializers.CharField(source='league.name', read_only=True)

    league = serializers.PrimaryKeyRelatedField(queryset=League.objects.all(), write_only=True)
    status = serializers.SerializerMethodField()
    home_score = serializers.SerializerMethodField()
    away_score = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        # Explicitly list fields for clarity and to include league_name
        fields = [
            'id', # Always good to include the ID
            'game_date',
            'game_time',
            'opponent',
            'location',
            'game_type',
            'league',         
            'league_name',  
            'status',         
            'home_score',     
            'away_score',  
        ]

    def get_status(self, obj):
        """
        Retrieves the game status from the related GameResult object.
        Handles cases where no GameResult exists yet.
        """
        try:
            # Access the related GameResult object via its related_name 'result'
            return obj.result.status
        except GameResult.DoesNotExist:
            # Fallback for upcoming games or games without recorded results
            game_datetime = datetime.datetime.combine(obj.game_date, obj.game_time)
            current_datetime = datetime.datetime.now()
            if current_datetime > game_datetime:
                return 'Upcoming' 
            else:
                return 'Upcoming'

    def get_home_score(self, obj):
        """
        Retrieves the home team's score from the related GameResult.
        Returns '-' if no GameResult exists.
        """
        try:
            return obj.result.home_score
        except GameResult.DoesNotExist:
            return '-'

    def get_away_score(self, obj):
        """
        Retrieves the away team's score from the related GameResult.
        Returns '-' if no GameResult exists.
        """
        try:
            return obj.result.away_score
        except GameResult.DoesNotExist:
            return '-'
        
    # --- Methods for determining team names and logos ---
    def get_home_team_name(self, obj):
        # If it's a HOME game for 'Clique Mambas', then 'Clique Mambas' is the home team.
        # Otherwise (it's an AWAY game for 'Clique Mambas'), the opponent is the home team.
        return 'Clique Mambas' if obj.game_type == 'HOME' else obj.opponent

    def get_away_team_name(self, obj):
        # If it's a HOME game for 'Clique Mambas', then the opponent is the away team.
        # Otherwise (it's an AWAY game for 'Clique Mambas'), 'Clique Mambas' is the away team.
        return obj.opponent if obj.game_type == 'HOME' else 'Clique Mambas'