from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def mascota(request):
    return render(request, 'login.html')

def prueba(request):
    return HttpResponse(request, "¡Bienvenido a Carlito!")

def login(request):
    return render(request, 'login.html')

def carlo(request):
    return render(request, 'carlo.html')

def stats(request):
    return render(request, 'stats.html')

def comer(request):
    return render(request, 'morfi.html')

def banio(request):
    return render(request, 'banio.html')

# def gym(request):
    # return render(request, 'gym.html')