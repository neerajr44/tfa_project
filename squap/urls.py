from django.urls import path

from . import views

urlpatterns = [
        path('map/', views.view_map, name='map'),
        path('sightings/stats', views.stats_page, name = 'stats')
        ]
