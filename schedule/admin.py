from django.contrib import admin
from .models import Schedule, League

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('opponent', 'game_date', 'location', 'game_type', 'league',)
    list_filter = ('game_type', 'league', 'game_date')
    search_fields = ('opponent', 'location')
    date_hierarchy = 'game_date'