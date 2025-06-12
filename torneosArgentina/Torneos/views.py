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
    Permite filtrar por tipo, año y si es offline usando parámetros GET.
    """
    torneos = Torneo.objects.all() # Inicia con todos los torneos

    selected_tipo = request.GET.get('tipo', '')
    selected_year = request.GET.get('year', '')
    # NUEVO: Obtener el estado de 'offline' del filtro
    selected_offline = request.GET.get('offline', '') 

    # Aplicar filtro por tipo si se seleccionó uno Y NO ES 'todas_las_competencias'
    if selected_tipo and selected_tipo != 'todas_las_competencias':
        torneos = torneos.filter(tipo=selected_tipo)

    # Aplicar filtro por año si se ingresó uno válido
    if selected_year and selected_year.isdigit():
        torneos = torneos.filter(fecha__year=int(selected_year))

    # NUEVO: Aplicar filtro por 'offline'
    if selected_offline == 'True': # Si el filtro es para mostrar solo torneos offline
        torneos = torneos.filter(es_offline=True)
    elif selected_offline == 'False': # Si el filtro es para mostrar solo torneos online
        torneos = torneos.filter(es_offline=False)


    selected_options = {
        'todas_las_competencias': (not selected_tipo or selected_tipo == 'todas_las_competencias'),
        'copa_america': (selected_tipo == 'Copa_America'),
        'copa': (selected_tipo == 'Copa'),
        'liga': (selected_tipo == 'Liga'),
        'superliga': (selected_tipo == 'Superliga'),
        'desafio': (selected_tipo == 'Desafio'),
        # CAMBIO: Ahora manejamos 'offline' en lugar de 'internacional'
        'offline_filter_active': (selected_offline == 'True'), # Para saber si el filtro offline está activo
        'online_filter_active': (selected_offline == 'False'), # Para saber si el filtro online está activo
    }
    

    context = {
        "torneos": torneos,
        "selected_tipo": selected_tipo,
        "selected_year": selected_year,
        "selected_offline": selected_offline, # Pasar el estado de offline seleccionado al template
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

# ELIMINAMOS torneos_internacionales porque ahora lo maneja el filtro 'offline'
# def torneos_internacionales(request):
#     """
#     Muestra solo torneos marcados como internacionales.
#     Asume que 'Internacional' es un valor del campo 'tipo' en tu modelo Torneo.
#     """
#     return lista_torneos(request, tipo="Internacional")


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
