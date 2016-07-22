
from django.db import models



class Estudiante(models.Model):


	cedula = models.CharField(max_length=10,unique=True)
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	correo = models.EmailField(max_length=30,blank=True,null=True)
	
	def __str__(self):
		return self.cedula

class Materia(models.Model):
	nombre = models.CharField(max_length=30,unique=True)
	cupo= models.IntegerField()

	def __str__(self):
		return self.nombre