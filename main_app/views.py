from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guitar
from django.views.generic import ListView

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
    return render(request, 'guitars/detail.html', {'guitar': guitar})