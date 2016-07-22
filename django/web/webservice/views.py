from estudiante.models import Estudiante
from estudiante.models import Materia
from .serializable import EstudianteSerializable
from .serializable import MateriaSerializable
from rest_framework import viewsets

class EstudianteViewSet(viewsets.ModelViewSet):
	
	serializer_class = EstudianteSerializable
	queryset=Estudiante.objects.all()

class MateriaViewSet(viewsets.ModelViewSet):
	serializer_class = MateriaSerializable
	queryset = Materia.objects.filter(cupo__gt=0,cupo__lte=30)
