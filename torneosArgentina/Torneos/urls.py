# Torneos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # Tu página de inicio
    
    # URL principal para la lista de torneos.
    # Ahora puede recibir tipo, año, y si es offline/online como parámetros GET.
    path("torneos/", views.lista_torneos, name="lista_torneos"),
    
    # URL para los detalles de un torneo específico.
    path("torneos/<int:torneo_id>/", views.detalle_torneos, name="detalle_torneos"),
    
    # Si 'desafios' es una vista separada que quieres mantener.
    path("desafios/", views.desafios, name="desafios"),
]
