from django.http.request import HttpRequest
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

class Guitar:
    def __init__(self, make, color, type):
        self.make = make
        self.color = color
        self.type = type

guitars = [
    Guitar('Unkown', 'Green', 'Telecaster'),
    Guitar('Fender', 'Orange Sunburst', 'Fender'),
    Guitar('Ibanez', 'Wood grain', 'Artcore')
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    return render(request, 'guitars/index.html', {'guitars': guitars})