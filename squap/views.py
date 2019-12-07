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

def main_one(request):
    squirrel='Squirrel Tracker'
    return render(request,'squap/main.html',{'Squirrel':squirrel})

def get_sighting(request):
    squirrels=Squirrel.objects.all()
    context={
        'squirrels':squirrels,
        }
    return render(request,'squap/sighting.html',context)

def update_squirrel(request,Unique_squirrel_ID):
    squirrel=Squirrel.objects.get(Unique_squirrel_ID=Unique_squirrel_ID)
    if request.method=="POST":
        form=SquirForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')

    else:
        form =SquirForm(instance=squirrel)
    context={
            'form':form
        }
    return render(request,'squap/edit.html',context)

def add_new_squirrel(request):
    if request.method=="POST":
        form=SquirForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')

    else:
        form=SquirForm()
    context={
            'form':form,
        }
    return render(request,'squap/edit.html',context)


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
