# Torneos/views.py

from django.shortcuts import render, get_object_or_404
from .models import Torneo, ImagenCarrusel, InformacionTorneoAnio # Asegúrate de importar todos los modelos necesarios

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
    Permite filtrar por tipo y año usando parámetros GET.
    """
    torneos = Torneo.objects.all() # Inicia con todos los torneos

    selected_tipo = request.GET.get('tipo', '')
    selected_year = request.GET.get('year', '')

    # Aplicar filtro por tipo si se seleccionó uno Y NO ES 'todas_las_competencias'
    if selected_tipo and selected_tipo != 'todas_las_competencias':
        torneos = torneos.filter(tipo=selected_tipo)

    # Aplicar filtro por año si se ingresó uno válido
    if selected_year and selected_year.isdigit():
        torneos = torneos.filter(fecha__year=int(selected_year))

    # --- INICIO DE CORRECCIÓN EN selected_options ---
    # Las claves del diccionario deben coincidir con cómo se acceden en el template (ej. selected_options.copa_america)
    selected_options = {
        'todas_las_competencias': (not selected_tipo or selected_tipo == 'todas_las_competencias'),
        # ERROR: La clave era 'Copa_America' (mayúsculas) y en HTML se usa 'copa_america' (minúsculas)
        'copa_america': (selected_tipo == 'Copa_America'), # Clave en minúsculas, valor de comparación con mayúsculas
        # ERROR: La clave era 'Copa' (mayúscula) y en HTML se usa 'copa' (minúscula)
        'copa': (selected_tipo == 'Copa'), # Clave en minúsculas, valor de comparación con mayúsculas
        # Lo mismo para las demás, asegurando que la clave del diccionario sea minúscula
        'liga': (selected_tipo == 'Liga'),
        'superliga': (selected_tipo == 'Superliga'),
        'desafio': (selected_tipo == 'Desafio'),
        'internacional': (selected_tipo == 'Internacional'),
    }
    # --- FIN DE CORRECCIÓN EN selected_options ---

    context = {
        "torneos": torneos,
        "selected_tipo": selected_tipo,
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


def torneos_internacionales(request):
    """
    Muestra solo torneos marcados como internacionales.
    Asume que 'Internacional' es un valor del campo 'tipo' en tu modelo Torneo.
    """
    return lista_torneos(request, tipo="Internacional")


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