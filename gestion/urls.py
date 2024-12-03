from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('trabajadores/', views.trabajadores, name='trabajadores'),
    path('dosis/', views.dosis, name='dosis'),
    path('insertar/', views.Crear_trabajador.as_view(), name='insertar'),
    path('insertar_dosis/', views.Insertar_dosis.as_view(), name='insertar_dosis'),
    path('editar_dosis/<int:pk>', views.Editar_dosis.as_view(), name='editar_dosis'),
    re_path(r'^editar_trabajador/(?P<pk>\d+)/update/$', views.Editar_trabajador.as_view(), name='editar_trabajador'),
    path('eliminar_trabajador/<int:id>', views.eliminar_trabajador, name='eliminar'),
    path('eliminar_dosis/<int:id>', views.eliminar_dosis, name='eliminar_dosis'),
    path('buscar/', views.buscar, name='buscar'),
]