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
            'id': p.id,
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
    ]
    
    return JsonResponse(data, safe=False)

def ver_productos(request):
    return render(request, 'ver.html')

import json

# Funcion que agrega un producto con un objeto json
def registrar_producto(request):
    #checar si nuestra request es de tipo post
    if request.method == 'POST':
        #quiere decir que si estoy manejando el request
        try:
            data = json.loads(request.body) #parametro es un texto que deberia ser un json
            producto = Producto.objects.create(
                nombre = data['nombre'],
                precio = data['precio'],
                imagen = data['imagen']
            ) #Create directamente mete el objeto en la DB
            return JsonResponse(
                {
                    'mensaje': 'Registro Exitoso',
                    'id': producto.id    
                }, status=201
            )
        except Exception as e:
            print(str(e))
            return JsonResponse(
                {
                    'error': str(e)    
                }, status = 400
            )
    # si no es POST el request
    return JsonResponse(
        {
            'error': 'El metodo no esta soportado'    
        }, status = 405
    )

from django.shortcuts import get_object_or_404

# Funciones para el metodo PUT
def actualizar_producto(request, id_producto):
    if request.method == 'PUT':
        producto = get_object_or_404(Producto,  id=id_producto)
        try:
            #la informacion de la modificacion del poducto viene del body del request
            data = json.loads(request.body)
            producto.nombre = data.get('nombre', producto.nombre)
            producto.precio = data.get('precio', producto.precio)
            producto.imagen = data.get('imagen', producto.imagen)
            producto.save()
            return JsonResponse(
                {
                    'mensaje': 'Producto actualizado correctamente'
                },
                status=200
            )
        except Exception as e:
            return JsonResponse(
                {
                    'error':str(e)
                },
                status=400
            )
    return JsonResponse(
        {
            'error':'Metodo no es PUT'
        },
        status=405
    )
# Funciones para Delete
def borrar_producto(request, id_producto):
    if request.method == 'DELETE':
        producto = get_object_or_404(Producto, id=id_producto)
        producto.delete() # <-- borra fisicamente el registro de la BD
        return JsonResponse({'mensaje': 'Producto eliminado correctamente'},status=200)
    return JsonResponse({'error': 'El metodo no es DELETE'}, status=405)
# Funcion adicional para GET (De retonar un producto especifico)
def obtener_producto(request, id_producto):
    if request.method == 'GET':
        producto = get_object_or_404(Producto, id=id_producto)
        data = {
            "id": producto.id,
            "nombre": producto.nombre,
            "precio": producto.precio,
            "imagen": producto.imagen
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'error':'El metodo no es GET'}, status=405)
