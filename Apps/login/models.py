from django.db import models
from Apps.auth_device.models import Device


# Create your models here.
class DeviceLogin(models.Model):
    device_temporal_token = models.CharField(max_length=100, ) 
    device_token = models.CharField(max_length=100, default='') 
    is_login =  models.BooleanField(default=False)