from django.contrib import admin

# Register your models here.
from .models import Disco, DiscoDestacado, RegistrarUsuario, Contacto

# admin.site.register(Disco)
@admin.register(Disco)
class DiscoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "estado", "fecha_publicacion", "autor"]
    list_filter = ["estado", "autor"]
    raw_id_fields = ["autor"]
    ordering = ["-fecha_publicacion"]
    actions = ['publicar_discos']

    def publicar_discos(self, request, queryset):
        queryset.update(estado=Disco.Estado.PUBLICADO)
    publicar_discos.short_description = "Publicar discos seleccionados"


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

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "profesion", "ubicacion", "linkedin", "behance", "instagram", "discord"]
    ordering = ["nombre"]