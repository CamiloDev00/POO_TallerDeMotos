from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Empleado, Motocicleta, Servicio, OrdenServicio

# 1. Le decimos a Django que el Empleado se mostrará como un "anexo" (Inline)
class EmpleadoInline(admin.StackedInline):
    model = Empleado
    can_delete = False
    verbose_name_plural = 'Datos del Empleado (MotoGPRO)'

# 2. Modificamos el administrador de Usuarios nativo de Django
class EmpleadoUserAdmin(UserAdmin):
    inlines = (EmpleadoInline, )

# 3. Desvinculamos el User tradicional y registramos el nuestro con superpoderes
admin.site.unregister(User)
admin.site.register(User, EmpleadoUserAdmin)

# Registramos el resto de tus modelos normalmente
admin.site.register(Motocicleta)
admin.site.register(Servicio)
admin.site.register(OrdenServicio)