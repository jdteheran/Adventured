
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from Apps.login.views import Device_Login_Token, is_Login_Device
from Apps.google_login.views import Bienvenido
from Apps.email_ad.views import enviar_correo
#from allauth.account.views import LoginView, SignupView 
from django.contrib.auth.views import LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from Apps.auth_device.views import Temporal_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('home/', Bienvenido),
    path('users/', Temporal_token),
    path('device_login/', Device_Login_Token),
    path('fast_login/', is_Login_Device),
    path('enviar_correo/', enviar_correo),
    #path('', LoginView.as_view(), name="custom_login" ),

    path('', 
        LoginView.as_view(
            template_name = 'index.html'
        ), 
        name = "login"
    ),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
