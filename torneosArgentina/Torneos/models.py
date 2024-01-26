from django.db import models

# Create your models here.

# torneos/models.py
from django.db import models


class Torneo(models.Model):
    tipo = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to="torneos/", blank=True, null=True)
    internacional = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    def fechas_disponibles(self):
        return [fecha.year for fecha in self.fechas.all()]
