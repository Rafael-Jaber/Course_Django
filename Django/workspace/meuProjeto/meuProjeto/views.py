from django.http import HttpResponse

def home(request):
    return HttpResponse('Ola Mundo!')

def clientes(request):
    return HttpResponse('<h1>View de clietnes.</h1>')