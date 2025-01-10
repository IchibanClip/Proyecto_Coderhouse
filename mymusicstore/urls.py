from django.urls import path

from . import views

app_name = "mymusicstore"

urlpatterns = [
    path("", views.catalogo, name="catalogo"),
    path("registrarusuario", views.registrarusuario, name="registrarusuario"),
]