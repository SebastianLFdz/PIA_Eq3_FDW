from django.contrib import admin # type: ignore
from .models import USUARIO, PEDIDOS

# Register your models here.
admin.site.register(USUARIO)

admin.site.register(PEDIDOS)