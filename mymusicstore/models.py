from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Disco(models.Model):
    class Estado(models.TextChoices):
        BORRADOR = 'B', 'Borrador'
        PUBLICADO = 'P', 'Publicado'
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
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

    def __str__(self):
        return f"{self.nombre} {self.apellido}"