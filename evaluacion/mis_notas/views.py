from django.shortcuts import render
from mis_notas.models import Listado, Notas
# Create your views here.

l = Listado()


def home(request):
    return render(request, 'mis_notas/home.html')


def notas(request):
    context = {'context': l.ordenarNotas()}
    return render(request, 'mis_notas/notas.html', context)


def nueva_nota(request):
    return render(request, 'mis_notas/nueva_nota.html')


def creacion_nota(request):
    titulo = request.POST.get('titulo')
    descripcion = request.POST.get('descripcion')
    importante = request.POST.get('importante')
    if importante == 'importante':
        importante = True
    else:
        importante = False
    n = Notas(titulo, descripcion, importante)

    response = l.agregar_nota(n)

    context = {'context': response}

    return render(request, 'mis_notas/creacion_nota.html', context)


def eliminacion_nota(request):
    titulo = request.POST.get('titulo')
    response = l.eliminar_nota(titulo)

    context = {'context': response}

    return render(request, 'mis_notas/eliminacion_nota.html', context)
