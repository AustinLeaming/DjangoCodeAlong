from django.db import models

# Create your models here.
class Guitar(models.Model):
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    age = models.IntegerField()


    def __str__(self):
        return self.name
        
class Tuning(models.Model):
    tune = models.CharField(max_length=1)
