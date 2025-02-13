from django.shortcuts import render, redirect
from .models import Categoria
from django.http import JsonResponse

from .forms import CategoriaForm

# vista que carga y muestra el formulario
def agregar_categoria(request):
    # checar si vengo del formulario
    if request.method == 'POST':
        # quiere decir que enviaron el form
        form = CategoriaForm(request.POST)
        # checar que sus datos esten bien
        if form.is_valid():
            form.save()
            return redirect('ver')
    # Que pasa si no fue que mandaron el form
    else:
        form = CategoriaForm()
    return render(request, 'agregar.html', {'form': form})

# Vista que devuelve las categorias como JSON
def lista_categorias(request):
    # Obtener todas las categorias de la base de datos
    categorias = Categoria.objects.all()
    
    # vamos a guardar los datos en un dict
    # este diccionario fue creado al aire y no es seguro
    data = [
        {
            'nombre': c.nombre,
            'descripcion': c.descripcion
        }
        for c in categorias
    ]
    
    return JsonResponse(data, safe=False)

def ver_categorias(request):
    return render(request, 'ver.html')

