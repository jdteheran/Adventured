import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.forms.models import model_to_dict

# Create your views here.

from Apps.auth_device.models import Device
from uuid import uuid4
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

 #Create your views here.
def Temporal_token(request):

    status = {
        'success': False,
        'message': '',
        'codigo': 0
    }

    try:
        data = json.loads(request.body)

        device_id = data['device_id']
        os = data['os']
        os_version = data['os_version']

        if not device_id:
            status['message'] = 'device_id no enviado'
            return JsonResponse(status)

        if not os:
            status['message'] = 'os no enviado'
            return JsonResponse(status)

        if not os_version:
            status['message'] = 'os_version no enviado'
            return JsonResponse(status)

        status['success'] = True

        try: 
            device = Device.objects.get(device_id=device_id)
            
            status['message'] = 'OK'
        except:
            token_generated = uuid4()

            device = Device(device_id=device_id, os=os, os_version=os_version,token=token_generated)

            device.save()

            status['message'] = 'dispotivo creado'
            
            
        respuesta = {
            'status': status,
            'temporal_token': device.token
        }

        return JsonResponse(respuesta)
    except:
        status['message'] = 'error en el json de entrada'
        return JsonResponse(status)