from django.db import models

from django.contrib.auth.models import User # <-- Importamos el usuario nativo de Django

class Empleado(models.Model):
    ROLES = [
        ('Mecanico', 'Mecánico'),
        ('Admin', 'Administrador'),
        ('Mostrador', 'Empleado de Mostrador')
    ]

    # 1. Creamos el vínculo Uno a Uno.
    # null=True y blank=True evitan errores con los empleados que ya creaste antes
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    # 2. Podemos quitar el campo "nombre" porque el modelo User ya tiene "first_name" y "last_name"
    rol = models.CharField(max_length=20, choices=ROLES, default='Mostrador')

    def __str__(self):
        # Mostramos el nombre de usuario de Django y el rol
        if self.usuario:
            return f"{self.usuario.first_name} ({self.usuario.username}) - {self.rol}"
        return f"Empleado sin usuario asignado - {self.rol}"

class Motocicleta(models.Model):
    patente = models.CharField(max_length=7, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    cilindrada = models.IntegerField()
    dni_cliente = models.IntegerField()

    def clasificar_cilindrada(self):
        if self.cilindrada <= 150:
            return "Baja (hasta 150cc)"
        elif self.cilindrada <= 250:
            return "Media (hasta 250cc)"
        else:
            return "Alta (+500cc)"

    def __str__(self):
        return f"{self.patente} | {self.marca} {self.modelo} | {self.cilindrada}cc"

class Servicio(models.Model):
    codigo = models.CharField(max_length=10, unique=True, help_text="Ej: S001")
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.codigo} - {self.nombre} (${self.precio_base})"

class OrdenServicio(models.Model):
    moto = models.ForeignKey(Motocicleta, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    # Solo permitimos asignar empleados que tengan el rol de Mecánico
    mecanico = models.ForeignKey(
        Empleado,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'rol': 'Mecanico'}
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden #{self.id} - Moto: {self.moto.patente} - Mecánico: {self.mecanico.nombre if self.mecanico else 'Sin asignar'}"