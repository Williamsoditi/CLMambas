from rest_framework import serializers
from .models import NewsArticle

class NewsArticleSerializer(serializers.ModelSerializer):
    published_date = serializers.DateTimeField(format="%B %d, %Y %I:%M %p", read_only=True)
    
    class Meta:
        model = NewsArticle
        fields = '__all__'