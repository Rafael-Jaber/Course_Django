from django.http import HttpResponse


def home(request):
    return HttpResponse('Ola Mundo!')

def clientes(request):
    return HttpResponse('<h1>View de clietnes.</h1>')

def cliente_detalhe(request, id):
    return HttpResponse('<h1>Cliente Detalhe: {}</h1>'.format(id))

def cliente_nome(reques, nome):
    return HttpResponse('<h1>Nome do cliente: {}</h1>'.format(nome))