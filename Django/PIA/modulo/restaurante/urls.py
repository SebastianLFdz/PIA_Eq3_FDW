from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("registrarUsuario/", views.registrarUsuario, name="registrarUsuario"),
    path("editarUsuario/<pIdUsuario>", views.editarUsuario, name="editarUsuario"),
    path("eliminarUsuario/<pIdUsuario>" , views.eliminarUsuario, name="eliminarUsuario"),
    path("leerUsuario/", views.leerUsuario, name="leerUsuario"),
    path("usuarios/", views.usuarios, name="usuarios"),
    path("iniciarsesion/", views.iniciarsesion, name="iniciarsesion"),
    path("pedidos_mesero/", views.pedidos_mesero, name="pedidos_meseros"),
    path("pedidos_chef/", views.pedidos_chef, name="pedidos_chef"),
    path("registrarpedido/", views.registrarpedido, name="registrarpedido"),
    path("encargarpedido/", views.encargarpedido, name="encargarpedido"),
    path("eliminarpedido/<pIdPedido>", views.eliminarPedido, name="eliminarpedido"),
    path("editarpedido/<pIdPedido>", views.editarPedido, name="editarpedido"),
    path("leerpedido/", views.leerPedido, name="leerpedido"),
    path("inicio_admin/", views.inicio_admin, name="inicio_admin"),
    path("aceptarpedido/<pIdPedido>", views.aceptarPedido, name="aceptarpedido"),
]