from django.contrib import admin

# Register your models here.
from .models import Disco, DiscoDestacado, RegistrarUsuario

# admin.site.register(Disco)
@admin.register(Disco)
class DiscoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "estado", "fecha_publicacion"]
    list_filter = ["estado", "autor"]
    raw_id_fields = ["autor"]
    ordering = ["-fecha_publicacion"]

@admin.register(DiscoDestacado)
class DiscoDestacadoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "estado"]
    list_filter = ["estado", "autor"]
    raw_id_fields = ["autor"]
    ordering = ["nombre"]

@admin.register(RegistrarUsuario)
class RegistrarUsuarioAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "email", "telefono", "direccion", "contrasena"]
    list_filter = ["estado"]
    ordering = ["nombre"]