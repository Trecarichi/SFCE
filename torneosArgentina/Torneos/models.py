from django.db import models

class Torneo(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    tipo = models.CharField(max_length=100)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    internacional = models.BooleanField(default=False)
    # Cambiamos ImageField por CharField para usar rutas estáticas
    imagen_estatica = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        help_text="Ruta a la imagen principal del torneo (ej. images/nombre_torneo.png). Debe estar en torneos/static/images/"
    )

    def __str__(self):
        return f"{self.nombre} ({self.fecha.year})"

    # Añade un related_name si aún no lo tienes para facilitar la relación inversa
    # Si ya existe, puedes dejarlo como está.
    # class Meta:
    #     ordering = ['-fecha'] # Puedes añadir un ordenamiento por defecto

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
    # Campo para la imagen estática de la edición anual
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


# ===========================================================================
# NUEVO MODELO: ImagenAdicionalTorneo
# Para permitir múltiples imágenes asociadas a un mismo Torneo
# ===========================================================================
class ImagenAdicionalTorneo(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name='imagenes_adicionales')
    # Campo para la ruta estática de la imagen adicional
    imagen_estatica = models.CharField(
        max_length=255, 
        help_text="Ruta a la imagen adicional (ej. images/galeria/torneo_foto1.png). Debe estar en torneos/static/images/galeria/"
    )
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    orden = models.IntegerField(default=0) # Para controlar el orden de visualización

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"Imagen adicional para {self.torneo.nombre} - {self.descripcion or self.imagen_estatica}"


class ImagenCarrusel(models.Model):
    titulo = models.CharField(max_length=200)
    # Campo para la ruta estática de la imagen del carrusel
    imagen_estatica = models.CharField(
        max_length=255, 
        help_text="Ruta a la imagen del carrusel (ej. images/carrusel/imagen1.png). Debe estar en torneos/static/images/carrusel/"
    )
    descripcion = models.TextField(blank=True, null=True)
    orden = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['orden']
        verbose_name_plural = "Imágenes del Carrusel"

    def __str__(self):
        return self.titulo
    
    # Método para previsualizar la imagen en el admin
    from django.utils.html import format_html
    def imagen_preview(self):
        if self.imagen_estatica:
            # Asegúrate de que esta ruta coincida con tu configuración de STATIC_URL
            return format_html('<img src="/static/{}" style="width: 100px; height: auto;" />', self.imagen_estatica)
        return "(Sin imagen)"
    imagen_preview.short_description = 'Previsualización'

