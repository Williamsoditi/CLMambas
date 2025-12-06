# results_app/admin.py
from django.contrib import admin
from .models import GameResult 

@admin.register(GameResult)
class GameResultAdmin(admin.ModelAdmin):
    # Fields to display in the list view of the admin
    list_display = (
        'schedule_display', # This refers to the method below
        'home_score',
        'away_score',
        'status',
        'recorded_at',
        'last_updated'
    )

    # Fields to filter by in the admin sidebar
    list_filter = (
        'status',
        'schedule__game_date', # Filter by game date from related schedule
        'schedule__league',    # Filter by league from related schedule
    )

    # Fields to search by
    search_fields = (
        'schedule__opponent', # Search by opponent name from related schedule
        'status',
    )

    # Fields to make read-only in the admin form
    readonly_fields = ('recorded_at', 'last_updated',)

    # --- IMPORTANT: Ensure this method is correctly indented INSIDE the class ---
    def schedule_display(self, obj):
        """
        Custom method to display the __str__ representation of the related Schedule object.
        """
        return str(obj.schedule)
    schedule_display.short_description = 'Schedule' # Column header name
    schedule_display.admin_order_field = 'schedule__game_date' # Allows sorting by game date