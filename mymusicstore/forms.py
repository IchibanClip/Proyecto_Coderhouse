from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
import re
from .models import RegistrarUsuario, Disco, DiscoDestacado, Contacto

class UsuarioForm(forms.ModelForm):
    email = forms.EmailField(
        validators=[EmailValidator(message="Ingrese un email válido con '@' y '.com'")],
        required=True,
        error_messages={'required': 'Este campo es obligatorio'}
    )

    class Meta:
        model = RegistrarUsuario
        fields = ['nombre', 'apellido', 'email', 'contrasena', 'telefono', 'direccion']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }
        error_messages = {
            'nombre': {'required': 'Este campo es obligatorio'},
            'apellido': {'required': 'Este campo es obligatorio'},
            'telefono': {'required': 'Este campo es obligatorio'},
            'direccion': {'required': 'Este campo es obligatorio'},
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
        if '@' not in email or not email.endswith('.com'):
            raise ValidationError("Ingrese un email válido con '@' y '.com'")
        if RegistrarUsuario.objects.filter(email=email).exists():
            raise ValidationError("Este email ya está en uso.")
        return email

class DiscoForm(forms.ModelForm):
    class Meta:
        model = Disco
        fields = ['nombre', 'precio', 'descripcion', 'imagen', 'estado']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError("El nombre es obligatorio.")
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is None or precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return precio
    
class DiscoDestacadoForm(forms.ModelForm):
    disco_id = forms.ChoiceField(
        choices=[],
        label="Seleccionar Disco",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = DiscoDestacado
        fields = ["disco_id", "estado"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['disco_id'].choices = [(disco.id, f"{disco.nombre} - S/{disco.precio}") for disco in Disco.objects.all()]

    def clean_disco_id(self):
        disco_id = self.cleaned_data.get('disco_id')
        if not disco_id:
            raise forms.ValidationError("Debe seleccionar un disco.")
        return disco_id

class EditarPerfilForm(forms.ModelForm):
    fecha_de_cumpleanios = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/YYYY'}),
        input_formats=['%d/%m/%Y']
    )

    class Meta:
        model = RegistrarUsuario
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion', 'biografia', 'fecha_de_cumpleanios', 'avatar']

class CambiarContrasenaForm(forms.Form):
    nueva_contrasena = forms.CharField(widget=forms.PasswordInput(), required=False)
    confirmar_contrasena = forms.CharField(widget=forms.PasswordInput(), required=False)

    def clean(self):
        cleaned_data = super().clean()
        nueva_contrasena = cleaned_data.get('nueva_contrasena')
        confirmar_contrasena = cleaned_data.get('confirmar_contrasena')

        if nueva_contrasena and nueva_contrasena != confirmar_contrasena:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cleaned_data
    
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'profesion', 'ubicacion', 'linkedin', 'behance', 'instagram', 'discord', 'imagen']

