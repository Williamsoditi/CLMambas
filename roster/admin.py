from django.contrib import admin
from .models import Player

# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'jersey_number', 'position' , 'height'),
    search_fields = ('first_name', 'last_name', 'jersey_number', 'position')
    list_filter = ('position',)
    ordering = ('jersey_number',)
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'jersey_number', 'position', 'height', 'image')
        }),
        ('Physical Attributes', {
            'fields': ('height', 'weight' ),
        }),
        ('Image', {
            'fields': ('image',),
        }),
    )   

