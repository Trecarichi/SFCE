# Torneos/views.py

from django.shortcuts import render, get_object_or_404
from .models import Torneo, ImagenCarrusel, InformacionTorneoAnio 

def index(request):
    """
    Vista para la página de inicio.
    Recupera las imágenes del carrusel activas y las pasa al template.
    """
    imagenes_carrusel = ImagenCarrusel.objects.filter(activo=True).order_by('orden')

    context = {
        'imagenes_carrusel': imagenes_carrusel,
    }
    return render(request, "index.html", context)

def lista_torneos(request):
    """
    Vista principal para listar torneos.
    Permite filtrar por tipo (incluyendo Offline/Online) y año usando parámetros GET.
    """
    torneos = Torneo.objects.all() # Inicia con todos los torneos

    selected_tipo = request.GET.get('tipo', '')
    selected_year = request.GET.get('year', '')

    # Lógica de filtrado combinada para 'tipo' y 'es_offline'
    if selected_tipo:
        if selected_tipo == 'Offline':
            torneos = torneos.filter(es_offline=True)
        elif selected_tipo == 'Online':
            torneos = torneos.filter(es_offline=False)
        elif selected_tipo != 'todas_las_competencias': # Si no es offline/online y no es "todas las competencias"
            torneos = torneos.filter(tipo=selected_tipo)

    # Aplicar filtro por año si se ingresó uno válido
    if selected_year and selected_year.isdigit():
        torneos = torneos.filter(fecha__year=int(selected_year))

    # El diccionario selected_options se simplifica ya que todo viene de 'selected_tipo'
    selected_options = {
        'todas_las_competencias': (not selected_tipo or selected_tipo == 'todas_las_competencias'),
        'copa_america': (selected_tipo == 'Copa_America'),
        'copa': (selected_tipo == 'Copa'),
        'liga': (selected_tipo == 'Liga'),
        'superliga': (selected_tipo == 'Superliga'),
        'desafio': (selected_tipo == 'Desafio'),
        'offline': (selected_tipo == 'Offline'), # Nuevo estado para la opción Offline
        'online': (selected_tipo == 'Online'),   # Nuevo estado para la opción Online
    }
    
    context = {
        "torneos": torneos,
        "selected_tipo": selected_tipo, # Sigue siendo el único parámetro de tipo
        "selected_year": selected_year,
        "selected_options": selected_options,
    }
    return render(request, "lista_torneos.html", context)


def lista_torneos_por_anio(request, year):
    """
    Muestra torneos por año específico.
    Redirige a la vista principal 'lista_torneos' para manejar el filtrado.
    """
    return lista_torneos(request, year=str(year))


def lista_torneos_por_tipo(request, tipo):
    """
    Muestra torneos por tipo específico.
    Redirige a la vista principal 'lista_torneos' para manejar el filtrado.
    """
    return lista_torneos(request, tipo=tipo)


def desafios(request):
    """
    Muestra solo torneos de tipo 'Desafío'.
    Redirige a la vista principal 'lista_torneos' para manejar el filtrado.
    """
    return lista_torneos(request, tipo="Desafio")


def detalle_torneos(request, torneo_id):
    """
    Muestra los detalles de un torneo específico.
    """
    torneo = get_object_or_404(Torneo, id=torneo_id)
    return render(request, "detalle_torneos.html", {"torneo": torneo})
