from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

from django.shortcuts import render, redirect
from .forms import ProductoForm

class ProductoViewSet(viewsets.ModelViewSet):
    # esta variable me dice de donde saco el modelo y la informacion de DB
    queryset = Producto.objects.all()
    
    # como serializar la informacion
    serializer_class = ProductoSerializer
    
    # como renderizar mis respuestas
    renderer_classes = [JSONRenderer]
    
    #permitir filtrar que metodos HTTP se pueden usar
    #por defecto si no la delcaro se ocupan todos (get, post, put, delete)
    #http_method_names = ['get', 'post', 'put', 'delete']
    
def agregar_view(request):
    form = ProductoForm()
    return render(request, 'agregar.html', {'form': form})