from django.db import models
from categoria.models import Categoria

class DetallesProducto(models.Model):
    descripcion = models.CharField(max_length=300)
    fecha_caducidad = models.DateField()
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)

# Create your models here.
class Producto(models.Model):
    #atributos de clase
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    
    #primer parametro es el modelo a relacionar, y despues la estrategia de borrado
    detalles_producto = models.OneToOneField(DetallesProducto, null=True, blank=True, on_delete=models.CASCADE)
    
    #relacion de uno a muchos
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    
    #relacion de muchos a muchos
    proveedor = models.ManyToManyField(Proveedor)
    
    #cuando se requiera usar una relacion se usa un campo:
    #OneToOneField (1 : 1)
    #ForeignKey (1 : M)
    #ManyToManyField (M : M)
    
    def __str__ (self):
        return self.nombre
    
    # Necesito una funcion que devuelva el objeto en fomra de Dict 
    
    def to_dict(self):
        return {
            # 'ClaveValor': 'Valor'
            'nombre': self.nombre,
            'precio': self.precio,
            'imagen': self.imagen
        }


