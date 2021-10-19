from django.db import models

# Create your models here.
class Guitar(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    age = models.IntegerField()
    
    # class Guitar:
    #     def __init__(self, name, make, color, type, age):
    #     self.name = name
    #     self.make = make
    #     self.color = color
    #     self.type = type
    #     self.age = age
