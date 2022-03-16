from django.db import models

# Create your models here.
class App(models.Model):
    token = models.CharField(max_length=100, )
    name = models.CharField(max_length=100, ) 
    version = models.CharField(max_length=100, )
    lenguaje = models.CharField(max_length=100, )
    