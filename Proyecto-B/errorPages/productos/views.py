from django.shortcuts import render, redirect
from .models import Producto
from django.http import JsonResponse

#from .forms import ProductoForm

# Create your views here.

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
