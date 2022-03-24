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
        'code': 0
    }

    if request.method == 'POST':
        try:
            data = json.loads(request.POST.get('form'))

            temporal_token = data['temporal_token']
            try:
                token = data['token']
            except:
                print('error')

            if not temporal_token:
                status['message'] = 'temporal token no enviado'
                respuesta = {
                    'status': status,
                    'token': '',
                    'action': {
                        'message': '',
                        'reset': False,
                        'block': False
                    }
                }
                return JsonResponse(respuesta)

            try:
                device = Device.objects.get(token=temporal_token)

                try:
                    device_bd = DeviceLogin.objects.get(device_temporal_token=temporal_token)

                    status['success'] = True
                    status['message'] = 'login exitoso'
                    respuesta = {
                        'status': status,
                        'token': device_bd.device_token,
                        'action': {
                            'message': '',
                            'reset': False,
                            'block': False
                        }
                    }
                    return JsonResponse(respuesta) 
                except:
                    deviceLogin = DeviceLogin(device_temporal_token=device.token, device_token=token,  is_login=True)
                    deviceLogin.save()

                    status['success'] = True
                    status['message'] = 'login exitoso'
                    respuesta = {
                        'status': status,
                        'token': token,
                        'action': {
                            'message': '',
                            'reset': False,
                            'block': False
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
                        'block': False
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
                    'block': False
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
                'block': False
            }
        }
        return JsonResponse(respuesta)

@csrf_exempt
def is_Login_Device(request):

    status = {
        'success': False,
        'message': '',
        'code': 0
    }

    user = {
        'email': 'jdteheran@uninorte.edu.co',
        'name': 'Juan Teheran',
        'bridthday': '',
        'region': 'Colombia',
    }

    if request.method == 'POST':

        status['success'] = True
        status['message'] = 'Usuario Logueado'

        respuesta = {
            'status': status,
            'user': user,
            'api_url': '/api'
        }

        return JsonResponse(respuesta)
    else:
        respuesta = {
            'status': status,
            'user': user,
            'api_url': ''
        }
        return JsonResponse(respuesta)

    


    