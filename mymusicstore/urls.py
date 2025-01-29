from django.urls import path

from . import views
from .views import CatalogoListView, DiscoDetailView, RegistrarDiscoCreateView, RegistrarDiscoDestacadoCreateView, DiscoDestacadoDetailView, DiscoUpdateView, DiscoDeleteView

app_name = "mymusicstore"

urlpatterns = [
    path("", CatalogoListView.as_view(), name="catalogo"),
    path("registrardisco", RegistrarDiscoCreateView.as_view(), name="registrardisco"),
    path("registrardiscodestacado", RegistrarDiscoDestacadoCreateView.as_view(), name="registrardiscodestacado"),
    path("detalle/<int:pk>/", DiscoDetailView.as_view(), name="detalle_disco"),
    path("detalle_destacado/<int:pk>/", DiscoDestacadoDetailView.as_view(), name="detalle_disco_destacado"),
    path("editar/<int:pk>/", DiscoUpdateView.as_view(), name="editar_disco"),
    path("eliminar/<int:pk>/", DiscoDeleteView.as_view(), name="eliminar_disco"),
    path("registrarusuario", views.registrarusuario, name="registrarusuario"),
    path("contacto", views.contacto, name="contacto"),
    path('perfil/<int:usuario_id>/', views.perfil_usuario, name='perfil_usuario'),
    path('iniciarsesion/', views.iniciarsesion, name='iniciarsesion'),
    path('cerrarsesion/', views.cerrarsesion, name='cerrarsesion'),
    path('perfil/<int:usuario_id>/editar/', views.editar_perfil, name='editar_perfil'),
]