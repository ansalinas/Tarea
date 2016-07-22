from django.shortcuts import render, redirect
from .models import Estudiante
from .models import Materia
from .forms import FormularioEstudiante
from .forms import FormularioMateria
from .forms import FormularioModificarEstudiante
from .forms import FormularioModificarMateria



def listar(request):
	estudiante = Estudiante.objects.all()
	materia = Materia.objects.all()
	context={
		'estudiante':estudiante,
		'materia': materia,
	}
	return render(request,"listar.html",context)

def crear(request):	
	f = FormularioEstudiante(request.POST or None)
	if request.method == 'POST':
		if f.is_valid():
			datos = f.cleaned_data
			es =Estudiante()
			es.c = datos.get("cedula")
			es.n = datos.get("nombre")
			es.a = datos.get("apellido")
			es.co = datos.get("correo")
			if(es.save()!=True):
				return redirect(listar)
	context ={
		'f':f,
	}
	return render (request,"crear.html", context)

def crearMateria(request):
	f = FormularioMateria(request.POST or None)

	if request.method=="POST":
		if f.is_valid():
			datos = f.cleaned_data
			m = Materia()
			m.nombre = datos.get("nombre")
			m.cupo = datos.get("cupo")
			if(m.save()!=True):
				return redirect(listar)
	context = {
		'f':f,
	}
	return render(request,"crearMateria.html",context)

def ModifEstudiante(request):
	estud = Estudiante.objects.get(cedula=request.GET['cedula'])
	f = FormularioModificarEstudiante(request.POST or None)

	f.fields["nombre"].initial = estud.nombre
	f.fields["apellido"].initial = estud.apellido
	f.fields["correo"].initial = estud.correo

	if f.is_valid():
		datos = f.cleaned_data
		estud.nombre = datos.get("nombre")
		estud.apellido = datos.get("apellido")
		estud.correo = datos.get("correo")
		estud.save()
		return redirect(listar)

	context = {
		'estud':estud,
		'f':f,
	}
	return render(request,"modificarEstudiante.html",context)

def ModificarMateria(request):
	mat = Materia.objects.get(nombre=request.GET['nombre'])
	f = FormularioModificarMateria(request.POST or None)

	f.fields["cupo"].initial = mat.cupo
	if f.is_valid():
		datos = f.cleaned_data
		mat.cupo = datos.get("cupo")
		mat.save()
		return redirect(listar)
	context={
		'mat':mat,
		'f':f,
	}
	return render(request,"ModificarMateria.html",context)

def EliminarEstudiante(request):
	estud = Estudiante.objects.get(cedula=request.GET['cedula'])
	estud.delete()
	return redirect(listar)

def EliminarMateria(request):
	mat = Materia.objects.get(nombre=request.GET['nombre'])
	mat.delete()
	return redirect(listar)


