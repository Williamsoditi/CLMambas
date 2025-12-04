from django.contrib import admin
from .models import NewsArticle

# Register your models here.
admin.site.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ('title', 'content')
    list_filter = ['published_date']
    date_hierarchy = 'published_date'
