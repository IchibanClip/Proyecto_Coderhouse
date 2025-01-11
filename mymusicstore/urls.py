from django.urls import path

from . import views

app_name = "mymusicstore"

urlpatterns = [
    path("", views.catalogo, name="catalogo"),
    path("registrarusuario", views.registrarusuario, name="registrarusuario"),
    path("registrardisco", views.registrardisco, name="registrardisco"),
    path("registrardiscodestacado", views.registrardiscodestacado, name="registrardiscodestacado"),

]