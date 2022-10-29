from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Ant, Food
from .forms import FeedingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def ants_index(request):
  ants = Ant.objects.all()
  return render(request, 'ants/index.html', {
    'ants': ants
  })

def ants_detail(request, ant_id):
  ant = Ant.objects.get(id=ant_id)
  # Get the foods the ant doesn't have
  # First, create a list of the food ids that the 
  # ant DOES have
  id_list = ant.foods.all().values_list('id')
  # Query for the foods whose ids are not in the id_list
  foods_ant_doesnt_have = Food.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(
    request,
    'ants/detail.html',
    {
      'ant': ant,
      'feeding_form': feeding_form,
      'foods': foods_ant_doesnt_have
    }
  )

class AntCreate(CreateView):
  model = Ant
  fields = ['name', 'species', 'description', 'age']
  # success_url = '/ants/'

  # def get_success_url(self):
  #   return f'/ants/{self.object.id}'

class AntUpdate(UpdateView):
  model = Ant
  # Let's disallow the renaming of a ant by
  # excluding the name field
  fields = ['species', 'description', 'age']

class AntDelete(DeleteView):
  model = Ant
  success_url = '/ants/'

def add_feeding(request, ant_id):
  # create a FeedingForm instance using
  # the data that was submitted via the form
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # can't save the form/object to the db
    # until we've assigned a ant_id
    new_feeding = form.save(commit=False)
    new_feeding.ant_id = ant_id
    new_feeding.save()
  return redirect('detail', ant_id=ant_id)

def assoc_food(request, ant_id, food_id):
  ant = Ant.objects.get(id=ant_id)
  ant.foods.add(food_id)
  return redirect('detail', ant_id=ant_id)

def unassoc_food(request, ant_id, food_id):
  Ant.objects.get(id=ant_id).foods.remove(food_id)
  return redirect('detail', nt_id=ant_id)

class FoodList(ListView):
  model = Food

class FoodDetail(DetailView):
  model = Food

class FoodCreate(CreateView):
  model = Food
  fields = '__all__'

class FoodUpdate(UpdateView):
  model = Food
  fields = ['name', 'color']

class FoodDelete(DeleteView):
  model = Food
  success_url = '/foods/'