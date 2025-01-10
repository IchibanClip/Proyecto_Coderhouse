from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
import re
from .models import RegistrarUsuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = RegistrarUsuario
        fields = ['nombre', 'apellido', 'email', 'contrasena', 'telefono', 'direccion']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        telefono_str = str(telefono)
        if not re.fullmatch(r'\d{9}', telefono_str):
            raise ValidationError('El teléfono debe tener exactamente 9 dígitos.')
        return telefono


    def clean_contrasena(self):
        contrasena = self.cleaned_data.get('contrasena')
        if len(contrasena) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
        return contrasena

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_validator = EmailValidator()
        email_validator(email)
        return email

    def clean(self):
        cleaned_data = super().clean()
        required_fields = ['nombre', 'apellido', 'direccion']
        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, 'Este campo no puede estar vacío.')
        return cleaned_data
