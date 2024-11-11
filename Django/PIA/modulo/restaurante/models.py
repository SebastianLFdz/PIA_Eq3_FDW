from django.db import models # type: ignore

# Create your models here.
class USUARIO(models.Model):
    IdUsuario = models.CharField(primary_key=True, max_length=10)
    NoEmpleado = models.CharField(max_length=10)
    Nombre = models.CharField(max_length=80)
    PrimerApellido = models.CharField(max_length=50)
    SegundoApellido = models.CharField(max_length=50)
    Contrasena = models.CharField(max_length=50)
    FechaRegistro = models.DateTimeField()

    def __str__(self):
        usuario_detalle = "({0}) {1} {2} {3} {4} {5}"
        return usuario_detalle.format(self.IdUsuario, self.NoEmpleado, self.Nombre, self.PrimerApellido, self.SegundoApellido, self.Contrasena)
    
class PEDIDOS(models.Model):
    IdPedido = models.CharField(primary_key=True, max_length=10)
    NoOrden = models.CharField(max_length=10)
    MeseroEncargado = models.CharField(max_length=80)
    Platillo = models.CharField(max_length=50)
    Bebida = models.CharField(max_length=50)
    Postre = models.CharField(max_length=50)
    HoraRegistro = models.TimeField()


    def __str__(self):
        alumno_detalle = "({0}) {1} {2} {3} {4}"
        return alumno_detalle.format(self.IdPedido, self.NoOrden, self.MeseroEncargado, self.Platillo, self.Bebida, self.Postre, self.HoraRegistro)