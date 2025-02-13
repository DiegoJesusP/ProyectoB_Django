from django.shortcuts import render, redirect
from .models import Producto
from django.http import JsonResponse

from .forms import ProductoForm

# Crear una vista que cargue y muestre el formulario
def agregar_producto(request):
    #checar si vengo del formulario
    if request.method == 'POST':
        #quiere decir que enviaron el form
        form = ProductoForm(request.POST)
        #checar que sus datos esten bien
        if form.is_valid():
            form.save()
            return redirect('ver')
    #Que pasa si no fue que mandaron el form
    else:
        form = ProductoForm()
    return render(request, 'agregar.html', {'form': form})

#Vista que devuelve los productos como JSON

def lista_productos(request):
    #Obtener todos los productos de la base de5 datos
    productos = Producto.objects.all()
    
    #vamos a guardar los datos en un dict
    #este diccionario fue creado al aire y no es seguro
    data = [
        {
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
    ]
    
    return JsonResponse(data, safe=False)

def ver_productos(request):
    return render(request, 'ver.html')
