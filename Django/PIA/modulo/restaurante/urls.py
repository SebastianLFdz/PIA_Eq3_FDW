from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("", views.home),
    path("registrarUsuario/", views.registrarUsuario),
    path("editarUsuario/<pIdUsuario>", views.editarUsuario),
    path("eliminarUsuario/<pIdUsuario>" , views.eliminarUsuario),
    path("leerUsuario/", views.leerUsuario)
]