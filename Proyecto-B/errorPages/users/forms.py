from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

import re

# Primer formulario
class CustomUserCreationForm(UserCreationForm):
    '''
    Correos electrónicos que no sean de UTEZ
    Números de teléfono de menos o más de 10 dígitos
    matrículas que no sean de UTEZ
    Meter contraseñas de menos de 8 caracteres (usando JS)
    Meter contraseñas que no incluyan 1 número, 1 letra mayúscula ni un carácter especial (usando JS)
    Además el formulario de registro de usuario y de login ahora tienen estilos de bootstrap
    '''
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese su contraseña",
                "title": "Necesitas definir una contraseña segura",
                "required": True,
            }
        ),
    )
    
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirme su contraseña",
                "title": "Repita la contraseña ingresada anteriormente",
                "required": True,
            }
        ),
    )
    
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']

        #Si quiero editar la forma de los inputs necesito widgets
        
        widgets = {
            #Cada uno de los widgets del MODELO
            'email': forms.EmailInput(
                #Caracteristicas del elemento visual
                attrs={
                    "class": "form-control",
                    "required": True,
                    "pattern": "^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$",
                    "title": "Debes ingresar un correo institucional de la UTEZ",
                    "placeholder": "Ej: 20223tn059@utez.edu.mx",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Ingrese su nombre",
                }
            ),
            "surname": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Ingrese su apellido",
                }
            ),
            "control_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Ingrese su número de control",
                }
            ),
            "age": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "placeholder": "Ingrese su edad",
                }
            ),
            "tel": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "required": True,
                    "pattern": "^[0-9]{10}$",
                    "title": "Debes ingresar un número de teléfono válido",
                    "placeholder": "Ingrese su número de teléfono",
                }
            ),
        }
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[a-zA-Z0-9._%+-]+@utez\.edu\.mx$', email):
            raise forms.ValidationError("El correo debe ser institucional (terminar en @utez.edu.mx).")
        return email

    def clean_tel(self):
        tel = self.cleaned_data.get('tel')
        if not re.match(r'^\d{10}$', tel):
            raise forms.ValidationError("El número de teléfono debe tener exactamente 10 dígitos.")
        return tel

    def clean_control_number(self):
        control_number = self.cleaned_data.get('control_number')
        if not re.match(r'^\d{8,10}$', control_number):  # Ajusta el patrón si es necesario
            raise forms.ValidationError("El número de control debe ser válido.")
        return control_number

    def clean_password1(self):
        password = self.cleaned_data.get("password1")

        if len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        
        if not any(char.isupper() for char in password):
            raise forms.ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise forms.ValidationError("La contraseña debe contener al menos un carácter especial (!@#$%^&*...)")
        
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden. Inténtalo de nuevo.")

        return cleaned_data


# FORMULARIO DE LOGIN
class CustomUserLoginForm(AuthenticationForm):
    pass