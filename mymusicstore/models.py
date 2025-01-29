from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Disco(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = 'B', 'Borrador'
        PUBLICADO = 'P', 'Publicado'
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = RichTextField()
    imagen = models.ImageField(upload_to='discos/', null=True, blank=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.BORRADOR)

    def __str__(self):
        return self.nombre
    
class DiscoDestacado(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = 'B', 'Borrador'
        PUBLICADO = 'P', 'Publicado'
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='discosdestacados/', null=True, blank=True)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.BORRADOR)

    def __str__(self):
        return self.nombre
    
class RegistrarUsuario(models.Model):
    class Estado(models.TextChoices):
        ACTIVO = 'A', 'Activo'
        INACTIVO = 'I', 'Inactivo'
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=50)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    fecha_de_cumpleanios = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    linkedin = models.URLField()
    behance = models.URLField()
    instagram = models.URLField()
    discord = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='contacto/', null=True, blank=True)

    def __str__(self):
        return self.nombre