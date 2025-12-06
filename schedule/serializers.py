from rest_framework import serializers
from .models import Schedule, League

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    league_name = serializers.CharField(source='league.name', read_only=True)
    league = serializers.PrimaryKeyRelatedField(queryset=League.objects.all(), write_only=True)
    
    class Meta:
        model = Schedule
        fields = '__all__'  

