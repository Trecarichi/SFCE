# Torneos/models.py

from django.db import models
from django.utils.html import format_html
from django.templatetags.static import static

class Torneo(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    tipo = models.CharField(max_length=100)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    # CAMBIO: Renombramos 'internacional' a 'es_offline'
    es_offline = models.BooleanField(
        default=False, 
        verbose_name="¿Es offline (presencial)?",
        help_text="Marca si el torneo es presencial/offline. Si no, se considera online."
    )
    imagen_estatica = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        help_text="Ruta a la imagen principal del torneo (ej. images/nombre_torneo.png). Debe estar en torneos/static/images/"
    )

    def __str__(self):
        return f"{self.nombre} ({self.fecha.year})"

class InformacionTorneoAnio(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name='informacion_por_anio')
    anio = models.IntegerField()
    campeon = models.CharField(max_length=200, blank=True, null=True)
    subcampeon = models.CharField(max_length=200, blank=True, null=True)
    participantes_cantidad = models.IntegerField(blank=True, null=True)
    resumen = models.TextField(blank=True, null=True)
    link_transmision = models.URLField(blank=True, null=True)
    fecha_exacta = models.DateField(blank=True, null=True)
    ubicacion_especifica = models.CharField(max_length=200, blank=True, null=True)
    imagen_edicion_estatica = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        help_text="Ruta a la imagen de la edición anual (ej. images/edicion_2023.png)"
    )

    class Meta:
        unique_together = ('torneo', 'anio')
        ordering = ['-anio']

    def __str__(self):
        return f"{self.torneo.nombre} - Edición {self.anio}"

class ImagenAdicionalTorneo(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name='imagenes_adicionales')
    imagen_estatica = models.CharField(
        max_length=255, 
        help_text="Ruta a la imagen adicional (ej. images/galeria/torneo_foto1.png). Debe estar en torneos/static/images/galeria/"
    )
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"Imagen adicional para {self.torneo.nombre} - {self.descripcion or self.imagen_estatica}"


class ImagenCarrusel(models.Model):
    titulo = models.CharField(max_length=200, blank=True, null=True)
    imagen_estatica = models.CharField(
        max_length=255, 
        help_text="Ruta a la imagen estática del carrusel (ej. images/carrusel/imagen1.png). Debe estar en torneos/static/images/carrusel/"
    )
    descripcion = models.TextField(blank=True, null=True)
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['orden']
        verbose_name_plural = "Imágenes del Carrusel"

    def __str__(self):
        return self.titulo if self.titulo else f"Imagen {self.id}"
    
    def imagen_preview(self):
        if self.imagen_estatica:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', static(self.imagen_estatica))
        return "(Sin imagen)"
    imagen_preview.short_description = 'Previsualización'
