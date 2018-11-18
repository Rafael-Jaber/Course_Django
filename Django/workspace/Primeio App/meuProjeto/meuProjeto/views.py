from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    sexo = 'h'
    nome = 'Aslam'
    lista = [
        {'nome': 'Rafael', 'sexo': 'm'},
        {'nome': 'Fulano', 'sexo': 'i'},
        {'nome': 'Brenda', 'sexo': 'f'}
    ]
    return render(request, 'index.html', {'sexo': sexo, 'nome': nome, 'lista': lista})

