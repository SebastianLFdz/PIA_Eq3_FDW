from django.db import models # type: ignore

# Create your models here.
class USUARIO(models.Model):

    posiciones = [
        ('C', 'Chef'),
        ('M', 'Mesero'),
        ('A', 'Administrador')
    ]

    IdUsuario = models.AutoField(primary_key=True)
    NoEmpleado = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=80)
    PrimerApellido = models.CharField(max_length=50)
    SegundoApellido = models.CharField(max_length=50)
    Contrasena = models.CharField(max_length=50)
    Posicion = models.CharField(max_length=1, choices=posiciones)
    FechaRegistro = models.DateTimeField()

    def __str__(self):
        usuario_detalle = "{0} {1} {2} {3} {4} {5} {6} {7}"
        return usuario_detalle.format(self.IdUsuario, self.NoEmpleado, self.Nombre, self.PrimerApellido, self.SegundoApellido, self.Contrasena, self.Posicion, self.FechaRegistro)
    
class PEDIDOS(models.Model):

    posiciones = [
        ('Pendiente', 'Pendiente'),
        ('Aceptado', 'Aceptado')
    ]

    IdPedido = models.AutoField(primary_key=True)
    NoOrden = models.CharField(max_length=10)
    MeseroEncargado = models.CharField(max_length=80)
    Mesa = models.CharField(max_length=10)
    Platillo = models.CharField(max_length=50)
    Bebida = models.CharField(max_length=50)
    Postre = models.CharField(max_length=50)
    Estatus = models.CharField(max_length=10, choices=posiciones)
    HoraRegistro = models.TimeField()


    def __str__(self):
        alumno_detalle = "{0} {1} {2} {3} {4} {5} {6} {7} {8}"
        return alumno_detalle.format(self.IdPedido, self.NoOrden, self.MeseroEncargado, self.Mesa, self.Platillo, self.Bebida, self.Postre, self.Estatus, self.HoraRegistro)