from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Squirrel

"""idef index(request):
    return HttpResponse("View is working well.")
"""

def view_map(request):
    sighting = Squirrel.objects.all()[:25]
    context = {
            'sightings': sighting,
            }
    return render( request, 'squap/map.html', context)
# Create your views here.
