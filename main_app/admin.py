from django.contrib import admin
from .models import Guitar, Tuning, Accessory

# Register your models here.
admin.site.register(Guitar)
admin.site.register(Tuning)
admin.site.register(Accessory)