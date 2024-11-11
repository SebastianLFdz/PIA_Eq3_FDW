from django.shortcuts import render, redirect # type: ignore
from django.contrib import messages # type: ignore
from . models import USUARIO, PEDIDOS

# Create your views here.
def home(request):
    lstUsuarios = USUARIO.objects.all()
    return render(request, "adminUsuarios.html", {"tblUsuarios": lstUsuarios})

# CREAR
def registrarUsuario(request):
    if request.method == 'POST':
        pIdUsuario = request.POST["txtId"]
        pNoEmpleado = request.POST["txtNoEmpleado"]
        pNombre = request.POST["txtNombre"]
        pPrimerApellido = request.POST["txtPrimerApellido"]
        pSegundoApellido = request.POST["txtSegundoApellido"]
        pContrasena = request.POST["txtContrasena"]
        pFechaRegistro = request.POST["txtFechaRegistro"]
        
        try:
            alumno = USUARIO.objects.create(
                IdUsuario = pIdUsuario,
                NoEmpleado = pNoEmpleado,
                Nombre = pNombre,
                PrimerApellido = pPrimerApellido,
                SegundoApellido = pSegundoApellido,
                Contrasena = pContrasena,
                FechaRegistro = pFechaRegistro)
            messages.success(request, "Usuario registrado correctamente")
        except Exception as e:
            messages.error(request, "Error al registrar el usuario")
        
        return redirect("/")
    else:
        messages.warning(request, "Error al procesar los datos")
        return redirect("/")

# EDITAR
def editarUsuario(request, pIdUsuario):
    usuario = USUARIO.objects.get(IdUsuario=pIdUsuario)
    return render(request,"editUsuario.html", {"usuario": usuario})

def leerUsuario(request):
    pIdUsuario = request.POST["txtId"]
    pNoEmpleado = request.POST["txtNoEmpleado"]
    pNombre = request.POST["txtNombre"]
    pPrimerApellido = request.POST["txtPrimerApellido"]
    pSegundoApellido = request.POST["txtSegundoApellido"]
    pContrasena = request.POST["txtContrasena"]
    pFechaRegistro = request.POST["txtFechaRegistro"]

    usuario = USUARIO.objects.get(IdUsuario = pIdUsuario)
    usuario.IdUsuario = pIdUsuario
    usuario.NoEmpleado = pNoEmpleado
    usuario.Nombre = pNombre
    usuario.PrimerApellido = pPrimerApellido
    usuario.SegundoApellido = pSegundoApellido
    usuario.Contrasena = pContrasena
    usuario.FechaRegistro = pFechaRegistro
    usuario.save()
    return redirect("/")

# ELIMINAR
def eliminarUsuario(request, pIdUsuario):
    usuario = USUARIO.objects.get(IdUsuario=pIdUsuario)
    usuario.delete()
    return redirect("/")