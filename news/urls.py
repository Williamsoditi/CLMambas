from django.urls import path, include
from .views import NewsArticleList, NewsArticleDetail

urlpatterns = [
    path('news/', NewsArticleList.as_view(), name='news-article-list'),
    path('news/<int:pk>/', NewsArticleDetail.as_view(), name='news-article-detail'),
]