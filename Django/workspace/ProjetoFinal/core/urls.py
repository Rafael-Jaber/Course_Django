from django.urls import path
from .views import (
    home,
    lista_pessoas,
    pessoa_nova,
    pessoa_update,
    lista_veiculos,
    veiculo_novo,
    veiculo_update,
    lista_movrotativos,
    mov_rotativos_novo,
    lista_mensalista,
    mensalista_novo,
    lista_movmensalista,
    movmensalista_novo
)


urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa_novo/', pessoa_nova, name='core_lista_pessoa_nova'),
    path('pessoa-update/<int:id>', pessoa_update, name='core_pessoa_update'),

    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo_novo/', veiculo_novo, name='core_lista_veiculo_novo'),
    path('veiculo_update/<int:id>', veiculo_update, name='core_veiculo_update'),

    path('mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mov-rot-novo/', mov_rotativos_novo, name='core_lista_movrotativos_novo'),

    path('mensalistas/', lista_mensalista, name='core_lista_mensalista'),
    path('mensalista_novo/', mensalista_novo, name='core_lista_mensalista_novo'),

    path('mov-men/', lista_movmensalista, name='core_lista_movmensalistas'),
    path('mov-men-novo/', movmensalista_novo, name='core_lista_movmensalistas_novo'),
]
