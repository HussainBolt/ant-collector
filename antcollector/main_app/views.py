from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Ant:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

ants = [
  Ant('Lolo', 'tabby', 'foul little demon', 3),
  Ant('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Ant('Raven', 'black tripod', '3 legged ant', 4)
]

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def ants_index(request):
  return render(request, 'ants/index.html', { 'ants': ants })