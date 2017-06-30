# Register your models here.

from django.contrib import admin
from .models import Auto
from .models import Cliente
from .models import Empleado
from .models import Empresa
from .models import Venta
from .models import Compra


admin.site.register(Auto)

admin.site.register(Cliente)

admin.site.register(Empleado)

admin.site.register(Empresa)

admin.site.register(Venta)

admin.site.register(Compra)






