from django.shortcuts import render
from .models import Ant

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def ants_index(request):
  ants = Ant.objects.all()
  return render(request, 'ants/index.html', { 'ants': ants })