
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')


def login_usuario(request):
    return render(request,'login_usuario.html')

def login_empresa(request):
    return render(request, 'login_empresa.html')