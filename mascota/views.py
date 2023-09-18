from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mascota(request):
    return render(request, 'login.html')

def prueba(request):
    return HttpResponse(request, "¡Bienvenido a Carlito!")

def login(request):
    return render(request, 'login.html')

def carlo(request):
    return render(request, 'carlo.html')
