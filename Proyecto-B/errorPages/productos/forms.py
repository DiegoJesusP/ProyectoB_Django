# Generar aquí todos los formularios HTML que vamos a ocupar
from django import forms
from .models import Producto

# Crear una clase para cada formulario que necesitemos
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        # que campos van a verse en mi formulario
        fields = ['nombre', 'precio', 'imagen']
        
        # Personalizar inputs
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Nombre del producto'
                }),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                }),
        }
        
        # Etiquetas
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto (MXN)',
            'imagen': 'URL de la imagen'
        }
        
        # Personalizar los mensajes de error
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio'
            },
            'precio': {
                'required': 'Este campo es obligatorio',
                'invalid': 'Por favor, ingresa un precio válido'
            },
            'imagen': {
                'required': 'Este campo es obligatorio'
            }
        }
