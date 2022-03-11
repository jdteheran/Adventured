from django.db import models

# Create your models here.

class Device(models.Model):
    device_id = models.CharField(max_length=100, ) 
    os = models.CharField(max_length=100, )
    os_version = models.CharField(max_length=100, )
    token = models.CharField(max_length=100, )
    

    

    
   