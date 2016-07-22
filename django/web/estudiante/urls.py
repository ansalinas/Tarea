from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'estudiante.views.listar'),
    url(r'^crear/$', 'estudiante.views.crear'),
    url(r'^crearMateria/$', 'estudiante.views.crearMateria'),
    url(r'^ModifEstudiante/$', 'estudiante.views.ModifEstudiante'),
    url(r'^ModificarMateria/$', 'estudiante.views.ModificarMateria'),
    url(r'^EliminarEstudiante/$', 'estudiante.views.EliminarEstudiante'),
    url(r'^EliminarMateria/$', 'estudiante.views.EliminarMateria'),
]