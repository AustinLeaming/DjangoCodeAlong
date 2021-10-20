from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Guitar
from django.views.generic import ListView

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