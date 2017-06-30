from django.db import models

# Create your models here.

class Auto(models.Model):
	marca = models.CharField(max_length=200)
	modelo = models.CharField(max_length=200)
	patente = models.CharField(max_length=200)
	tipo = models.CharField(max_length=200)
	color = models.CharField(max_length=200)
	precio = models.DecimalField(max_digits=20, decimal_places=10)
	def __str__(self):
		return self.marca + " " + self.modelo + " - $" + "{0:.2f}".format(self.precio)

class Cliente(models.Model):
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	DNI = models.CharField(max_length=200)
	localidad = models.CharField(max_length=200)
	telefono = models.CharField(max_length=200)

class Empleado(models.Model):
        nombre = models.CharField(max_length=200)
        apellido = models.CharField(max_length=200)
        DNI = models.CharField(max_length=200)
        fecha_de_ingreso_de_trabajo = models.CharField(max_length=200)

class Empresa(models.Model):
        compra_registrada = models.CharField(max_length=200)
        ingressar_o_eliminar_vehiculo = models.CharField(max_length=200)
        ingresar_o_eliminar_cliente = models.CharField(max_length=200)
	ventas_reguistrada = models.CharField(max_length=200)

class Venta(models.Model):
        fecha_venta = models.CharField(max_length=200)

class Compra(models.Model):
        fecha_de_compra = models.CharField(max_length=200)
        ingressar_o_eliminar_vehiculo = models.CharField(max_length=200)
        ingresar_o_eliminar_cliente = models.CharField(max_length=200)
        ventas_reguistrada = models.CharField(max_length=200)

