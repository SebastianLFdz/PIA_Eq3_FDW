from django.shortcuts import render, redirect # type: ignore
from django.contrib import messages # type: ignore
from . models import USUARIO, PEDIDOS # type: ignore

# Create your views here.
def home(request):
    lstUsuarios = USUARIO.objects.all()
    return render(request, "adminUsuarios.html", {"tblUsuarios": lstUsuarios})

# REGISTRO DE USUARIOS
def usuarios(request):
    return render(request, "registro.html")

# CREAR USUARIO
def registrarUsuario(request):
    if request.method == 'POST':
        pIdUsuario = request.POST["txtNoEmpleado"]
        pNoEmpleado = request.POST["txtNoEmpleado"]
        pNombre = request.POST["txtNombre"]
        pPrimerApellido = request.POST["txtPrimerApellido"]
        pSegundoApellido = request.POST["txtSegundoApellido"]
        pContrasena = request.POST["txtContrasena"]
        pPosicion = request.POST["txtPosicion"]
        pFechaRegistro = request.POST["txtFechaRegistro"]
        
        try:
            alumno = USUARIO.objects.create(
                IdUsuario = pIdUsuario,
                NoEmpleado = pNoEmpleado,
                Nombre = pNombre,
                PrimerApellido = pPrimerApellido,
                SegundoApellido = pSegundoApellido,
                Contrasena = pContrasena,
                Posicion = pPosicion,
                FechaRegistro = pFechaRegistro)
            messages.success(request, "Usuario registrado correctamente")
        except Exception as e:
            messages.error(request, "Error al registrar el usuario")
        
        return redirect("/")
    else:
        messages.warning(request, "Error al procesar los datos")
        return redirect("/")

# EDITAR USUARIO
def editarUsuario(request, pIdUsuario):
    usuario = USUARIO.objects.get(IdUsuario=pIdUsuario)
    return render(request,"editUsuario.html", {"usuario": usuario})

# LEER USUARIO
def leerUsuario(request):
    pIdUsuario = request.POST["txtId"]
    pNoEmpleado = request.POST["txtNoEmpleado"]
    pNombre = request.POST["txtNombre"]
    pPrimerApellido = request.POST["txtPrimerApellido"]
    pSegundoApellido = request.POST["txtSegundoApellido"]
    pContrasena = request.POST["txtContrasena"]
    pPosicion = request.POST["txtPosicion"]
    pFechaRegistro = request.POST["txtFechaRegistro"]

    usuario = USUARIO.objects.get(IdUsuario = pIdUsuario)
    usuario.IdUsuario = pIdUsuario
    usuario.NoEmpleado = pNoEmpleado
    usuario.Nombre = pNombre
    usuario.PrimerApellido = pPrimerApellido
    usuario.SegundoApellido = pSegundoApellido
    usuario.Contrasena = pContrasena
    usuario.Posicion = pPosicion
    usuario.FechaRegistro = pFechaRegistro
    usuario.save()
    return redirect("/inicio_admin")

# ELIMINAR USUARIO
def eliminarUsuario(request, pIdUsuario):
    usuario = USUARIO.objects.get(IdUsuario=pIdUsuario)
    usuario.delete()
    return redirect("/inicio_admin")

# INICIAR SESION
def iniciarsesion(request):
    if request.method == 'POST':
        pNoEmpleado = request.POST["txtNoEmpleado"]
        messages.get_messages(request)
        pContrasena = request.POST["txtContrasena"]
        messages.get_messages(request)
        try:
            usuario = USUARIO.objects.get(NoEmpleado=pNoEmpleado)

            if usuario.Contrasena == pContrasena:
                request.session['posicion'] = usuario.Posicion.lower()
                
                posicion_usuario = usuario.Posicion.lower()

                if posicion_usuario == 'c':
                    return redirect("/pedidos_chef")
                elif posicion_usuario == 'm':
                    return redirect("/pedidos_mesero")
                elif posicion_usuario == 'a':
                    return redirect("/inicio_admin")
                else:
                    return redirect("/")
            else:
                messages.error(request, "Contraseña incorrecta")
                return redirect("/")

        except USUARIO.DoesNotExist:
            messages.error(request, "Usuario no encontrado")
            return redirect("/")
        
    return render(request,"adminUsuarios.html")
    
# PEDIDOS PARA MESEROS
def pedidos_mesero(request):
    return render(request, "pedidos_meseros.html", {"tblPedidos": PEDIDOS.objects.all()})

# PEDIDOS PARA CHEFS
def pedidos_chef(request):
    return render(request, "pedidos_chef.html", {"tblPedidos": PEDIDOS.objects.all()})

# ELIMINAR PEDIDOS DE MESEROS
def eliminarPedido(request, pIdPedido):
    pedido = PEDIDOS.objects.get(IdPedido=pIdPedido)
    if pedido.Estatus == "Aceptado":
        return redirect("/pedidos_mesero")
    else:
        pedido.delete()
    return redirect("/pedidos_mesero")

# INICIO DE ADMINISTRADOR
def inicio_admin(request):
    return render(request, "admin_root.html", {"tblUsuarios": USUARIO.objects.all()})

# ENCARGAR PEDIDOS DE MESEROS
def encargarpedido(request):
    return render(request, "encargarpedido.html")   

# EDITAR PEDIDOS DE MESEROS
def editarPedido(request, pIdPedido):
    pedido = PEDIDOS.objects.get(IdPedido=pIdPedido)
    return render(request,"editPedido.html", {"tblpedido": pedido})

# LEER PEDIDOS DE MESEROS Y CHEFS
def leerPedido(request):
    pIdPedido = request.POST["txtNoOrden"]
    pNoOrden = request.POST["txtNoOrden"]
    pMeseroEncargado = request.POST["txtMeseroEncargado"]
    pMesa = request.POST["txtMesa"]
    pPlatillo = request.POST["txtPlatillo"]
    pBebida = request.POST["txtBebida"]
    pPostre = request.POST["txtPostre"]
    pEstatus = request.POST["txtEstatus"]
    pHoraRegistro = request.POST["txtHoraRegistro"]

    pedido = PEDIDOS.objects.get(NoOrden = pNoOrden)
    pedido.IdPedido = pIdPedido
    pedido.NoOrden = pNoOrden
    pedido.MeseroEncargado = pMeseroEncargado
    pedido.Mesa = pMesa
    pedido.Platillo = pPlatillo
    pedido.Bebida = pBebida
    pedido.Postre = pPostre
    pedido.Estatus = pEstatus
    pedido.HoraRegistro = pHoraRegistro
    pedido.save()
    return redirect("/pedidos_mesero")

# REGISTRAR PEDIDOS DE MESEROS
def registrarpedido(request):
    if request.method == 'POST':
        pIdPedido = request.POST["txtNoOrden"]
        pNoOrden = request.POST["txtNoOrden"]
        pMeseroEncargado = request.POST["txtMeseroEncargado"]
        pMesa = request.POST["txtMesa"]
        pPlatillo = request.POST["txtPlatillo"]
        pBebida = request.POST["txtBebida"]
        pPostre = request.POST["txtPostre"]
        pEstatus = request.POST["txtEstatus"]
        pHoraRegistro = request.POST["txtHoraRegistro"]
        
        try:
            pedido = PEDIDOS.objects.create(
                IdPedido = pIdPedido,
                NoOrden = pNoOrden,
                MeseroEncargado = pMeseroEncargado,
                Mesa = pMesa,
                Platillo = pPlatillo,
                Bebida = pBebida,
                Postre = pPostre,
                Estatus = pEstatus,
                HoraRegistro = pHoraRegistro)
            return redirect("/pedidos_mesero")
        except Exception as e:
            messages.error(request, "Error al registrar el pedido")
        
        return redirect("/")
    else:
        messages.warning(request, "Error al procesar los datos")
        return redirect("/")
    
def aceptarPedido(request, pIdPedido):
    pedido = PEDIDOS.objects.get(IdPedido=pIdPedido)
    pedido.Estatus = "Aceptado"
    pedido.save()
    return redirect("/pedidos_chef")