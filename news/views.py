from django.shortcuts import render
from rest_framework import generics
from .models import NewsArticle
from .serializers import NewsArticleSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

# Create your views here.
class NewsArticleList(generics.ListCreateAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

class NewsArticleDetail(generics.RetrieveAPIView):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE', 'PATCH']:
            return  [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]