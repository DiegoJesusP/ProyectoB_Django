# Generar todos los formularios HTML que vamos a ocupar
from django import forms
from .models import Categoria

# Crear una clase para cada formulario que necesitemos
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        # que campos van a verse en mi formulario
        fields = ['nombre', 'imagen']
        
        # Personalizar inputs
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la categoría'
                }),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'URL de la imagen'
                })
        }
        
        # Etiquetas
        labels = {
            'nombre': 'Nombre de la categoría',
            'imagen': 'URL de la imagen'
        }
        
        # Personalizar los mensajes de error
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio'
            },
            'imagen': {
                'required': 'Este campo es obligatorio'
            }
        }