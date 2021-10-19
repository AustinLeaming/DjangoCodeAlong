from django.http.request import HttpRequest
from django.shortcuts import render

# add the following import 
from django.http import HttpResponse

# Create your views here.


# defined the home view 
def home(request):
    return HttpRequest('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')