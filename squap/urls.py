from django.urls import path

from . import views

app_name='squap'

urlpatterns = [
        path('map/', views.view_map, name='map'),
        path('',views.main_one, name='main'),
        path('sightings/',views.get_sighting,name='sighting'),
        path('sightings/<str:Unique_squirrel_ID>/',views.update_squirrel,name='edit_sighting'),
        path('sightings/add',views.add_new_squirrel,name='add_sighting'),
        path('sightings/stats', views.stats_page, name = 'stats')
        ]
