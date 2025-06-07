# Torneos/models.py

from django.db import models

class Torneo(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=[
        ('todas_las_competencias', 'Todas las competencias'),
        ('Copa_America', 'Copa América'),   
        ('Copa', 'Copa'),
        ('Liga', 'Liga'),
        ('Superliga', 'Superliga'),
        ('Desafio', 'Desafío'),
        ('Internacional', 'Internacional'),
    ])
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    internacional = models.BooleanField(default=False)
    
    imagen_estatica = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Ruta a la imagen estática del torneo (ej. 'images/nombre_torneo.png'). Debe estar en Torneos/static/images/"
    )

    def __str__(self):
        return f"{self.nombre} ({self.fecha.year})"

    class Meta:
        verbose_name = "Torneo Principal"
        verbose_name_plural = "Torneos Principales"


class ImagenCarrusel(models.Model):
    titulo = models.CharField(max_length=200, blank=True, null=True)
    # ¡CAMBIO CRÍTICO AQUÍ! De ImageField a CharField
    imagen_estatica = models.CharField( # CAMBIADO EL NOMBRE A imagen_estatica para coherencia
        max_length=255,
        help_text="Ruta a la imagen estática del carrusel (ej. 'images/carrusel/imagen1.jpg'). Debe estar en Torneos/static/images/carrusel/"
    )
    descripcion = models.TextField(blank=True, null=True)
    orden = models.IntegerField(default=0, help_text="Define el orden en el carrusel")
    activo = models.BooleanField(default=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['orden']
        verbose_name_plural = "Imágenes de Carrusel"

    def __str__(self):
        return self.titulo if self.titulo else f"Imagen {self.id}"

    # La previsualización ahora usará la ruta estática
    def imagen_preview(self):
        from django.utils.html import mark_safe
        from django.templatetags.static import static
        if self.imagen_estatica:
            return mark_safe(f'<img src="{static(self.imagen_estatica)}" style="width: 50px; height: auto;" />')
        return ""
    imagen_preview.short_description = 'Previsualización'


class InformacionTorneoAnio(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name='informacion_por_anio')
    anio = models.IntegerField()
    campeon = models.CharField(max_length=100)
    subcampeon = models.CharField(max_length=100, blank=True, null=True)
    participantes_cantidad = models.IntegerField(blank=True, null=True)
    resumen = models.TextField(blank=True, null=True)

    link_transmision = models.URLField(max_length=500, blank=True, null=True,
                                        help_text="Enlace a la transmisión del torneo (Twitch, YouTube, etc.)")
    fecha_exacta = models.DateField(blank=True, null=True,
                                    help_text="Fecha específica de esta edición anual del torneo.")
    ubicacion_especifica = models.CharField(max_length=100, blank=True, null=True,
                                            help_text="Ubicación específica para esta edición anual.")

    imagen_edicion_estatica = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Ruta a la imagen estática de esta edición (ej. 'images/edicion_2023.png'). Debe estar en Torneos/static/images/"
    )


    class Meta:
        unique_together = ('torneo', 'anio')
        verbose_name_plural = "Información de Torneo por Año"
        ordering = ['-anio'] # Ordenar por año descendente en el admin

    def __str__(self):
        return f"{self.torneo.nombre} - {self.anio}"
