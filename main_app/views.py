from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Location

# Create your views here.
def home(request):
    return render(request, 'home.html')

class LocationList(ListView):
    model = Location
    fields = ['name', 'category', 'city', 'state']