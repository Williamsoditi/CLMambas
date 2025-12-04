from django.contrib import admin
from .models import Player

# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'jersey_number', 'position' , 'height_ft', 'weight_kgs')
    search_fields = ('name', 'jersey_number', 'position')
    list_filter = ('position',)
    ordering = ('jersey_number',)
    fieldsets = (
        ('Athlete Data', {
            'fields': ('name', 'jersey_number', 'position')
        }),
        ('Physical Attributes', {
            'fields': ('height_ft', 'weight_kgs'),
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )   

