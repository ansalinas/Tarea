from rest_framework import serializers
from estudiante.models import Estudiante 
from estudiante.models import Materia 


class EstudianteSerializable(serializers.ModelSerializer):
	class Meta:
		model = Estudiante
		fields = ('cedula','nombre','apellido')




class MateriaSerializable(serializers.ModelSerializer):
	class Meta:
		model = Materia 
		fields = ("nombre","cupo")
