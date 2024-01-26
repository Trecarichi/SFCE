from django.shortcuts import render, get_object_or_404
from .models import Torneo


def index(request):
    return render(request, "index.html", {})


def lista_torneos(request):
    torneos = Torneo.objects.all()
    return render(request, "lista_torneos.html", {"torneos": torneos})


def lista_torneos_por_anio(request, year):
    torneos = Torneo.objects.filter(fecha__year=year)
    return render(request, "lista_torneos.html", {"torneos": torneos})


def lista_torneos_por_tipo(request, tipo):
    torneos = Torneo.objects.filter(tipo=tipo)
    return render(request, "lista_torneos.html", {"torneos": torneos})


def torneos_internacionales(request):
    torneos = Torneo.objects.filter(internacional=True)
    return render(request, "lista_torneos.html", {"torneos": torneos})


def desafios(request):
    torneos = Torneo.objects.filter(tipo="Desafío")
    return render(request, "lista_torneos.html", {"torneos": torneos})


def detalle_torneos(request, torneo_id):
    torneo = get_object_or_404(Torneo, id=torneo_id)
    return render(request, "detalle_torneos.html", {"torneo": torneo})


# En tu vista que renderiza esta plantilla
def buscar_torneos(request):
    # Obtener la lista de años de tus torneos
    years = Torneo.objects.values_list("fecha__year", flat=True).distinct()
    return render(request, "buscar_torneos.html", {"years": years})


from django.shortcuts import redirect, get_object_or_404
from .models import Torneo


def buscar_por_anio(request):
    if request.method == "GET":
        year = request.GET.get("year")
        torneo = get_object_or_404(Torneo, fecha__year=year)
        return redirect("detalle_torneos", torneo_id=torneo.id)


def buscar_por_tipo(request, tipo):
    return render(request, "buscar_por_tipo.html", {"tipo": tipo})


def buscar_por_tipo_y_anio(request, tipo):
    return render(request, "buscar_por_tipo_y_anio.html", {"tipo": tipo})


def buscar_torneos_internacionales(request):
    return render(request, "buscar_torneos_internacionales.html", {})


def vista_que_renderiza_template(request):
    # Código para obtener el objeto Torneo, por ejemplo:
    torneo = Torneo.objects.get(id=1)  # Aquí necesitas obtener el objeto Torneo adecuado

    return render(request, "buscar_por_anio.html", {"torneo": torneo})
