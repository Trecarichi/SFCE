from django.shortcuts import render, get_object_or_404
from .models import Torneo, ImagenCarrusel # Asegúrate de importar ImagenCarrusel

# No necesitas Q para esta solución específica, pero si lo usas en otras partes, déjalo.
# from django.db.models import Q

def index(request):
    """
    Vista para la página de inicio.
    Recupera las imágenes del carrusel activas y las pasa al template.
    """
    # Filtra las imágenes activas y las ordena por el campo 'orden'
    # Esto asumirá que ya subiste imágenes y marcaste 'activo=True' en el admin.
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

    # Obtener los parámetros de filtro de la URL. Si no se pasan, serán ''.
    selected_tipo = request.GET.get('tipo', '')
    selected_year = request.GET.get('year', '')

    # Aplicar filtro por tipo si se seleccionó uno
    if selected_tipo:
        torneos = torneos.filter(tipo=selected_tipo)

    # Aplicar filtro por año si se ingresó uno válido
    if selected_year and selected_year.isdigit(): # Asegura que sea un número
        torneos = torneos.filter(fecha__year=int(selected_year))

    # --- ¡CÓDIGO AGREGADO PARA ELIMINAR EL ERROR DE SINTAXIS EN EL TEMPLATE! ---
    # Este diccionario nos permitirá pasar booleanos claros al template,
    # evitando errores de sintaxis en las comparaciones.
    selected_options = {
        'todos': not selected_tipo, # Es True si selected_tipo es una cadena vacía
        'copa': (selected_tipo == 'Copa'),
        'liga': (selected_tipo == 'Liga'),
        'superliga': (selected_tipo == 'Superliga'),
        'desafio': (selected_tipo == 'Desafío'),
        'internacional': (selected_tipo == 'Internacional'),
    }
    # --- FIN CÓDIGO AGREGADO ---

    # Prepara el contexto para la plantilla
    context = {
        "torneos": torneos,
        "selected_tipo": selected_tipo, # Todavía útil para el JavaScript inicial del template
        "selected_year": selected_year, # Para que el input de año recuerde el valor
        "selected_options": selected_options, # ¡El nuevo diccionario con booleanos!
    }
    return render(request, "lista_torneos.html", context)


def lista_torneos_por_anio(request, year):
    """
    Muestra torneos por año específico.
    Redirige a la vista principal 'lista_torneos' para manejar el filtrado.
    """
    # Llama a la vista principal, pasando el año como parámetro GET
    return lista_torneos(request, year=str(year))


def lista_torneos_por_tipo(request, tipo):
    """
    Muestra torneos por tipo específico.
    Redirige a la vista principal 'lista_torneos' para manejar el filtrado.
    """
    # Llama a la vista principal, pasando el tipo como parámetro GET
    return lista_torneos(request, tipo=tipo)


def torneos_internacionales(request):
    """
    Muestra solo torneos marcados como internacionales.
    Asume que 'Internacional' es un valor del campo 'tipo' en tu modelo Torneo.
    """
    # Si 'Internacional' es un valor del campo 'tipo', redirige a la vista principal
    return lista_torneos(request, tipo="Internacional")


def desafios(request):
    """
    Muestra solo torneos de tipo 'Desafío'.
    Redirige a la vista principal 'lista_torneos' para manejar el filtrado.
    """
    return lista_torneos(request, tipo="Desafío")


def detalle_torneos(request, torneo_id):
    """
    Muestra los detalles de un torneo específico.
    """
    torneo = get_object_or_404(Torneo, id=torneo_id)
    return render(request, "detalle_torneos.html", {"torneo": torneo})


# --- Vistas que probablemente son redundantes y puedes considerar eliminar ---
# Si la lógica principal de búsqueda está en `lista_torneos`, estas ya no serían necesarias.
# def buscar_torneos(request): ...
# def buscar_por_anio(request): ...
# def buscar_por_tipo(request, tipo): ...
# def buscar_por_tipo_y_anio(request, tipo): ...
# def buscar_torneos_internacionales(request): ...
# def vista_que_renderiza_template(request): ... (Si solo era un ejemplo de testing)