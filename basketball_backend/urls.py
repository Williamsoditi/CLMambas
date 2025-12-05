from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('api/', include('news.urls')),
    path('api/', include('schedule.urls')),
    path('api/', include('roster.urls')),
    #Add DRF auth token urls for admin login/logout
    path('api-auth/', include('rest_framework.urls') ), 
]
