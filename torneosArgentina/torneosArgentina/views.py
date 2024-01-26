# torneosArgentina/views.py
from django.shortcuts import render


def index(request):
    return render(request, "torneosArgentina/Torneos/template/index.html")


def lista_torneos(request):
    # Lógica para obtener la lista de torneos, similar a tu implementación
    torneos = [...]
    return render(request, "torneosArgentina/Torneos/template/lista_torneos.html", {"torneos": torneos})


def detalle_torneos(request, torneo_id):
    # Lógica para obtener detalles de un torneo, similar a tu implementación
    torneo = {...}
    return render(request, "torneosArgentina/Torneos/detalle_torneos.html", {"torneo": torneo})
