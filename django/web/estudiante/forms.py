from django import forms
from .models import Estudiante
from .models import Materia




class FormularioEstudiante(forms.ModelForm):
	class Meta:
		model = Estudiante
		fields=["cedula","nombre","apellido","correo"]


class FormularioMateria(forms.ModelForm):
	class Meta:
		model = Materia
		fields=["nombre","cupo"]


class FormularioModificarEstudiante(forms.ModelForm):
	class Meta:
		model = Estudiante
		fields=["nombre","apellido","correo"]

class FormularioModificarMateria(forms.ModelForm):
	class Meta:
		model = Materia
		fields=["cupo"]