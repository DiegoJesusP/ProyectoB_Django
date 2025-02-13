from django.db import models

# Create your models here.

class Categoria(models.Model):
    # atributos de clase
    nombre = models.CharField(max_length=100)
    imagen = models.URLField()
    
    def __str__(self):
        return self.nombre
    
    # Necesito una funcion que devuelva el objeto en forma de Dict
    
    def to_dict(self):
        return {
            # 'ClaveValor': 'Valor'
            'nombre': self.nombre,
            'imagen': self.imagen
        }
