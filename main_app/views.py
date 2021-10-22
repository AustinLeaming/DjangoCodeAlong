from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guitar, Accessory
from django.views.generic import ListView, DetailView
from .forms import TuningForm

def assoc_accessory(request, guitar_id, accessory_id):
    Guitar.objects.get(id=guitar_id).accessories.add(accessory_id)
    return redirect('detail', guitar_id=guitar_id)

class GuitarUpdate(UpdateView):
    model = Guitar
    fields = ['name', 'age', 'color']

class GuitarDelete(DeleteView):
    model = Guitar
    success_url = '/guitars/'

class GuitarCreate(CreateView):
    model = Guitar
    fields = '__all__'

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', {'guitars': guitars})

def guitars_detail(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    tuning_form = TuningForm()
    accessories_guitar_doesnt_have = Accessory.objects.exclude(id__in = guitar.accessories.all().values_list('id'))
    return render(request, 'guitars/detail.html', {'guitar': guitar, 'tuning_form': tuning_form, 'accessories': accessories_guitar_doesnt_have})

def add_tuning(request, guitar_id):
    # create a modelForm instance using the data in request.POST
    form = TuningForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it has the cat_id is assigned
        new_tuning = form.save(commit=False)
        new_tuning.guitar_id = guitar_id
        new_tuning.save()
    return redirect('detail', guitar_id=guitar_id)

class AccessoryList(ListView):
      model = Accessory

class AccessoryDetail(DetailView):
  model = Accessory

class AccessoryCreate(CreateView):
  model = Accessory
  fields = '__all__'

class AccessoryUpdate(UpdateView):
  model = Accessory
  fields = ['name', 'description']

class AccessoryDelete(DeleteView):
  model = Accessory
  success_url = '/accessories/'