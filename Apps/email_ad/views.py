from django.shortcuts import render
from django.http import JsonResponse

import smtplib

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
 #Create your views here.
def enviar_correo(request):
    status = {
        'success': True,
        'message': 'Correo enviado',
        'code': 200
    }

    mensaje = "Subject: {}\n\n{}".format('Correo de prueba','Este es un correo enviado desde la aplicacion de adventured django')
    emisor = 'adventureddjango@gmail.com'
    password = 'adventured123'
    receptor = 'oliver.sitan@eyeflytech.com'

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(emisor,password)

    servidor.sendmail(emisor , receptor, mensaje)

    servidor.quit()

    return JsonResponse(status)
