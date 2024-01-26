from django.urls import path
from . import views
from django.contrib import admin

app_name = "Torneos"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("lista_torneos/", views.lista_torneos, name="lista_torneos"),
    path("lista_torneos/por_anio/<int:year>/", views.lista_torneos_por_anio, name="lista_torneos_por_anio"),
    path("lista_torneos/por_tipo/<str:tipo>/", views.lista_torneos_por_tipo, name="lista_torneos_por_tipo"),
    path("torneos_internacionales/", views.torneos_internacionales, name="torneos_internacionales"),
    path("desafios/", views.desafios, name="desafios"),
    path("detalle_torneos/", views.detalle_torneos, name="detalle_torneos"),
    path("buscar_torneos/", views.buscar_torneos, name="buscar_torneos"),
    path("buscar_torneos/por_anio/<int:year>/", views.buscar_por_anio, name="buscar_por_anio"),
    path("buscar_torneos/por_tipo/<str:tipo>/", views.buscar_por_tipo, name="buscar_por_tipo"),
    path(
        "buscar_torneos/internacionales/", views.buscar_torneos_internacionales, name="buscar_torneos_internacionales"
    ),
]
