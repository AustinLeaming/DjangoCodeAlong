from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guitar
from django.views.generic import ListView
from .forms import TuningForm

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
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', {'guitars': guitars})

def guitars_detail(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    tuning_form = TuningForm()
    return render(request, 'guitars/detail.html', {'guitar': guitar, 'tuning_form': tuning_form})

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