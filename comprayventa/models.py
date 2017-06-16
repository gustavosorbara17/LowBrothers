from django.db import models

# Create your models here.

class auto(models.Model):
	marca = models.CharField(max_length=200)
	modelo = models.CharField(max_length=200)
	patente = models.CharField(max_length=200)
	tipo = models.CharField(max_length=200)
	color = models.CharField(max_length=200)
	precio = models.DecimalField(max_digits=20, decimal_places=10)
