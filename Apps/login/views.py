import json
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from Apps.login.models import DeviceLogin
from Apps.auth_device.models import Device

@csrf_exempt

 #Create your views here.
def Device_Login_Token(request):

    status = {
        'success': False,
        'message': '',
        'codigo': 0
    }

    if request.method == 'POST':

        try:
            data = json.loads(request.body)

            token = data['token']

            if not token:
                status['message'] = 'token no enviado'
                respuesta = {
                    'status': status,
                    'token': token,
                    'action': {
                        'message': '',
                        'reset': False,
                        'bloqueo': False
                    }
                }
                return JsonResponse(respuesta)

            try:
                device = Device.objects.get(token=token)

                try:
                    device_bd = DeviceLogin.objects.get(device_token=token)
                    device_bd.is_login = True
                    device_bd.save()

                    status['success'] = True
                    status['message'] = 'login exitoso'
                    respuesta = {
                        'status': status,
                        'token': token,
                        'action': {
                            'message': '',
                            'reset': False,
                            'bloqueo': False
                        }
                    }
                    return JsonResponse(respuesta) 
                except:
                    deviceLogin = DeviceLogin(device_token=device.token, is_login=True)
                    deviceLogin.save()

                    status['success'] = True
                    status['message'] = 'login exitoso'
                    respuesta = {
                        'status': status,
                        'token': token,
                        'action': {
                            'message': '',
                            'reset': False,
                            'bloqueo': False
                        }
                    }
                    return JsonResponse(respuesta)   
            except:
                status['message'] = 'token no asociado a ningun dispositivo'
                respuesta = {
                    'status': status,
                    'token': '',
                    'action': {
                        'message': '',
                        'reset': False,
                        'bloqueo': False
                    }
                }
                return JsonResponse(respuesta)    
        except:
            status['message'] = 'json invalido'
            respuesta = {
                'status': status,
                'token': '',
                'action': {
                    'message': '',
                    'reset': False,
                    'bloqueo': False
                }
            }
            return JsonResponse(respuesta)
        
    else:
        status['message'] = 'no se admite metodo diferente de post'
        respuesta = {
            'status': status,
            'token': '',
            'action': {
                'message': '',
                'reset': False,
                'bloqueo': False
            }
        }
        return JsonResponse(respuesta)

@csrf_exempt
def is_Login_Device(request):

    status = {
        'success': False,
        'message': '',
        'codigo': 0
    }

    if request.method == 'POST':




        
        return JsonResponse(status)
    else:
        respuesta = {
            'status': status,
            'user': '',
            'api_url': ''
        }
        return JsonResponse(respuesta)

    


    