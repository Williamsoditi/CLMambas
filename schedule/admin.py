from django.contrib import admin
from .models import Schedule


# Register your models here.
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
        list_display = ('opponent', 'game_date', 'location', 'home_game')
        list_filter = ('home_game', 'game_date')
        search_fields = ('opponent','location')
        date_hierarchy = 'game_date'