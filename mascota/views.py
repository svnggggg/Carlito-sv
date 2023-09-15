from django.shortcuts import render

# Create your views here.

def mascota(request):
    return render(request, 'login.html')