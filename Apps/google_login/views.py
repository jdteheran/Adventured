from django.shortcuts import render

 #Create your views here.
def Bienvenido(request):
    return render(request, 'welcome.html')