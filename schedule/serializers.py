from rest_framework import serializers
from .models import Schedule

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'  