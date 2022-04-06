import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.forms.models import model_to_dict
from Apps.app.models import App

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
        'code': 200
    }

    try:

        #un algoritmo desencriptar(request.POST.get('form'))

        data = json.loads(request.POST.get('form'))

        device = data['device']
        app = data['app']

        if not device:
            status['message'] = 'device no enviado'
            status['code'] = 500
            return JsonResponse({
            'status':status
            })

        if not app:
            status['message'] = 'app no enviada'
            status['code'] = 500
            return JsonResponse({
            'status':status
            })

        name = app['name']
        version = app['version']
        language = app['language']

        if not name:
            status['message'] = 'app name no enviada'
            status['code'] = 500
            return JsonResponse({
            'status':status
            })

        if not version:
            status['message'] = 'app verision no enviado'
            status['code'] = 500
            return JsonResponse({
            'status':status
            })

        if not language:
            status['message'] = 'app lenfuaje no enviado'
            status['code'] = 500
            return JsonResponse({
            'status':status
            })
        
        print('hola')

        device_id = device['device_id']
        os = device['os']
        os_version = device['os_version']

        if not device_id:
            status['message'] = 'device device_id no enviado'
            status['code'] = 500
            return JsonResponse({
            'status':status
            })

        if not os:
            status['message'] = 'device os no enviado'
            status['code'] = 500
            return JsonResponse({
            'status':status
            })

        if not os_version:
            status['message'] = 'device os_version no enviado'
            status['code'] = 500
            return JsonResponse({
            'status':status
            })

        status['success'] = True

        try: 
            device = Device.objects.get(device_id=device_id)
            
            status['message'] = 'OK'
        except:
            token_generated = uuid4()

            device = Device(device_id=device_id, os=os, os_version=os_version,token=token_generated)

            device.save()

            app = App(token=token_generated, name=name, version=version, language=language)

            app.save()

            status['message'] = 'dispotivo creado'
            
            
        respuesta = {
            'status': status,
            'temporal_token': device.token
        }

        return JsonResponse(respuesta)
    except:
        status['message'] = 'error en el json de entrada'
        status['code'] = 500
        return JsonResponse({
            'status':status
            })