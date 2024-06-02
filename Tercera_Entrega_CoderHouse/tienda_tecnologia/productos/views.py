from django.shortcuts import render, redirect, get_object_or_404
from .models import Celular, Computadora, Televisor
from .forms import CelularForm, ComputadoraForm, TelevisorForm

def inicio(request):
    celulares = Celular.objects.all()
    computadoras = Computadora.objects.all()
    televisores = Televisor.objects.all()
    return render(request, 'productos/inicio.html', {
        'celulares': celulares,
        'computadoras': computadoras,
        'televisores': televisores
    })

def listar_celulares(request):
    celulares = Celular.objects.all()
    return render(request, 'productos/listar_celulares.html', {'celulares': celulares})

def listar_computadoras(request):
    computadoras = Computadora.objects.all()
    return render(request, 'productos/listar_computadoras.html', {'computadoras': computadoras})

def listar_televisores(request):
    televisores = Televisor.objects.all()
    return render(request, 'productos/listar_televisores.html', {'televisores': televisores})

def agregar_producto(request):
    tipo = request.GET.get('tipo')
    if tipo == 'celular':
        form = CelularForm()
    elif tipo == 'computadora':
        form = ComputadoraForm()
    elif tipo == 'televisor':
        form = TelevisorForm()
    else:
        form = None
    
    if request.method == 'POST':
        if tipo == 'celular':
            form = CelularForm(request.POST)
        elif tipo == 'computadora':
            form = ComputadoraForm(request.POST)
        elif tipo == 'televisor':
            form = TelevisorForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('inicio')
    
    return render(request, 'productos/agregar_producto.html', {'form': form, 'tipo': tipo})

def detalle_producto(request, tipo, id):
    if tipo == 'celular':
        producto = get_object_or_404(Celular, id=id)
    elif tipo == 'computadora':
        producto = get_object_or_404(Computadora, id=id)
    elif tipo == 'televisor':
        producto = get_object_or_404(Televisor, id=id)
    else:
        producto = None
    
    return render(request, 'productos/detalle_producto.html', {'producto': producto, 'tipo': tipo})

def buscar_productos(request):
    query = request.GET.get('q')
    resultados_celulares = Celular.objects.filter(marca__icontains=query) if query else []
    resultados_computadoras = Computadora.objects.filter(marca__icontains=query) if query else []
    resultados_televisores = Televisor.objects.filter(marca__icontains=query) if query else []
    
    return render(request, 'productos/buscar.html', {
        'query': query,
        'resultados_celulares': resultados_celulares,
        'resultados_computadoras': resultados_computadoras,
        'resultados_televisores': resultados_televisores,
    })
