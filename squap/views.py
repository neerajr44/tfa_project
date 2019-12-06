from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("View is working well.")

# Create your views here.
