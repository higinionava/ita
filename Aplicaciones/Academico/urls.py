from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('hogar/', views.hogar),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('inscribirCurso/', views.inscribirCurso),
    path('inscripcionCurso/', views.inscripcionCurso),
    path('inicio/', views.inicio),
]