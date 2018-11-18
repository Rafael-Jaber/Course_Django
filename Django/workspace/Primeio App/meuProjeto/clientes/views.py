from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def clientes(request):
    return HttpResponse('<h1>View de clietnes.</h1>')

def cliente_detalhe(request, id):
    return HttpResponse('<h1>Cliente Detalhe: {}</h1>'.format(id))

def cliente_nome(reques, nome):
    return HttpResponse('<h1>Nome do cliente: {}</h1>'.format(nome))