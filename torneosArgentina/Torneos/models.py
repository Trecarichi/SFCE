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
        ('Desafio', 'Desafío'), # <-- NOTA: Si usas 'Desafío' en el admin y quieres que el filtro funcione, el valor interno debe ser 'Desafio' (sin tilde) para que coincida con el HTML y la vista. O usar 'Desafío' consistentemente en todas partes.
        ('Internacional', 'Internacional'),
    ])
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    internacional = models.BooleanField(default=False)
    imagen_torneo = models.ImageField(upload_to='torneos_imagenes/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.fecha.year})"

    class Meta:
        verbose_name = "Torneo Principal"
        verbose_name_plural = "Torneos Principales"


class ImagenCarrusel(models.Model):
    titulo = models.CharField(max_length=200, blank=True, null=True)
    imagen = models.ImageField(upload_to='carrusel_imagenes/')
    descripcion = models.TextField(blank=True, null=True)
    orden = models.IntegerField(default=0, help_text="Define el orden en el carrusel")
    activo = models.BooleanField(default=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['orden']
        verbose_name_plural = "Imágenes de Carrusel"

    def __str__(self):
        return self.titulo if self.titulo else f"Imagen {self.id}"

    def imagen_preview(self):
        if self.imagen:
            from django.utils.html import mark_safe
            return mark_safe(f'<img src="{self.imagen.url}" style="width: 50px; height: auto;" />')
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

    # --- CAMPO NUEVO (PARA LA IMAGEN DE LA EDICIÓN) ---
    imagen_edicion = models.ImageField(upload_to='ediciones_fotos/', blank=True, null=True,
                                       help_text="Imagen representativa de esta edición anual del torneo.")


    class Meta:
        unique_together = ('torneo', 'anio')
        verbose_name_plural = "Información de Torneo por Año"
        ordering = ['-anio'] # Ordenar por año descendente en el admin

    def __str__(self):
        return f"{self.torneo.nombre} - {self.anio}"