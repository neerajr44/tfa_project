from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Squirrel
from .forms import SquirForm

"""idef index(request):
    return HttpResponse("View is working well.")
"""

def view_map(request):
    sighting = Squirrel.objects.all()[:25]
    context = {
            'sightings': sighting,
            }
    return render( request, 'squap/map.html', context)


def stats_page(request):
    am_count = 0
    pm_count = 0
    running_count = 0
    foraging_count = 0
    approaches_count = 0
    moans_count = 0
    sq_count = len( Squirrel.objects.distinct('Unique_squirrel_ID'))
    context = {'squirrel_count' : sq_count,
              'AM_count' : am_count,
              'PM_count' : pm_count,
              'Running_count' : running_count,
              'Foraging_count' : foraging_count,
              'Approaches_count' : approaches_count,
              'Moans_count' : moans_count,
              }
    return render(request, 'squap/stats.html', context)
# Create your views here.
