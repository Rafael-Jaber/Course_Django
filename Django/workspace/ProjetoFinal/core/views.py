from django.shortcuts import render, redirect

from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
)

from .form import (
    PessoaForm,
    VeiculoForm,
    MovRotativosForm,
    MensalistaForm,
    MovmensalistaForm
)


def home(request):
    context = {'mensagem': 'Ola mundo'}
    return render(request, 'core/index.html', context)


# CRUD PESSOA


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


def pessoa_nova(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


# CRUD VEICULOS


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculos')


def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)


def lista_movrotativos(request):
    movRotativos = MovRotativo.objects.all()
    form = MovRotativosForm
    data = {'mov_rot': movRotativos, 'form': form}
    return render(request, 'core/lista_movrotativos.html', data)

def mov_rotativos_novo(request):
    form = MovRotativosForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movrotativos')


def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm
    data = {'mov_men': mensalistas, 'form': form}
    return render(request, 'core/lista-mensalista.html', data)

def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mensalista')


def lista_movmensalista(request):
    movMensalista = MovMensalista.objects.all()
    form = MovmensalistaForm
    data = {'mov_mensalista': movMensalista, 'form': form}
    return render(request, 'core/lista_movmensalistas.html', data)

def movmensalista_novo(request):
    form = MovmensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_movmensalistas')