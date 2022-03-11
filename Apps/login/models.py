from django.db import models
from Apps.auth_device.models import Device


# Create your models here.
class DeviceLogin(models.Model):
    device_token = models.CharField(max_length=100, ) 
    is_login =  models.BooleanField(default=False)