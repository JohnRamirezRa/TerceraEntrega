from django.shortcuts import render, HttpResponse
from register.models import Usuarios

def register(request):
    return render(request, 'register.html')

def index(request):
    return render(request, 'index.html')

def tables(request):

    usuarios=Usuarios.objects.all()
    return render(request, 'tables.html', {"usuarios": usuarios})
# Create your views here.
