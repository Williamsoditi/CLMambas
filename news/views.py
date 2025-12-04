from django.shortcuts import render
from rest_framework import generics
from .models import NewsArticle
from .serializers import NewsArticleSerializer

# Create your views here.
class NewsArticleList(generics.ListCreateAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

class NewsArticleDetail(generics.RetrieveAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer