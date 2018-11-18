from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    sexo = 'h'
    nome = 'Aslam'
    return render(request, 'index.html', {'sexo': sexo, 'nome': nome})

