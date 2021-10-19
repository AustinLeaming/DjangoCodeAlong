from django.http.request import HttpRequest
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Guitar:
    def __init__(self, name, make, color, type, age):
        self.name = name
        self.make = make
        self.color = color
        self.type = type
        self.age = age

guitars = [
    Guitar('No name', 'Unknown', 'Green', 'Telecaster', 1),
    Guitar('Ophelia', 'Fender', 'Orange Sunburst', 'Stratocaster', 12),
    Guitar('Artie', 'Ibanez', 'Wood grain', 'Artcore', 1)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    return render(request, 'guitars/index.html', {'guitars': guitars})