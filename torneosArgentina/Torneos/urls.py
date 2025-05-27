# Torneos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # Tu página de inicio
    
    # URL principal para la lista de torneos, ahora puede recibir tipo y año como parámetros GET
    path("torneos/", views.lista_torneos, name="lista_torneos"),
   
    # Si quieres mantener URLs "limpias" para cada tipo o año específico (útil para marcadores, SEO)
    path("torneos/anio/<int:year>/", views.lista_torneos_por_anio, name="lista_torneos_por_anio"),
    path("torneos/tipo/<str:tipo>/", views.lista_torneos_por_tipo, name="lista_torneos_por_tipo"),
    path("torneos/internacionales/", views.torneos_internacionales, name="torneos_internacionales"),
    path("torneos/desafios/", views.desafios, name="desafios"),
    path("torneos/<int:torneo_id>/", views.detalle_torneos, name="detalle_torneos"),
    
    # Estas URLs específicas para "buscar_por_anio" y "buscar_por_tipo" pueden eliminarse
    # si la lógica se centraliza en 'lista_torneos' que usa parámetros GET.
    #path("buscar_por_anio/", views.buscar_por_anio, name="buscar_por_anio"),
    #path("buscar_por_tipo/<str:tipo>/", views.buscar_por_tipo, name="buscar_por_tipo"),
    #path("buscar_por_tipo_y_anio/<str:tipo>/", views.buscar_por_tipo_y_anio, name="buscar_por_tipo_y_anio"),
    #path("buscar_torneos_internacionales/", views.buscar_torneos_internacionales, name="buscar_torneos_internacionales"),
    #path("vista_que_renderiza_template/", views.vista_que_renderiza_template, name="vista_que_renderiza_template"),
]