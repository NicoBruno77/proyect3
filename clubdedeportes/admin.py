from django.contrib import admin
from .models import Residente, Invitado, Empleados, Sector
# Register your models here.


admin.site.register(Residente)
admin.site.register(Invitado)
admin.site.register(Empleados)
admin.site.register(Sector)