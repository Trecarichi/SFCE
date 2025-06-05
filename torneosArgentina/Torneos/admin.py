from django.contrib import admin
from django.utils.html import format_html # Importa format_html
from .models import Torneo, ImagenCarrusel, InformacionTorneoAnio

# Clase para personalizar la visualización de Torneo en el admin
@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
    # Asegúrate de que list_display usa los nuevos nombres de campo y el método de previsualización
    list_display = ('nombre', 'fecha', 'tipo', 'ubicacion', 'internacional', 'imagen_estatica_display') 
    search_fields = ('nombre', 'tipo', 'ubicacion')
    list_filter = ('fecha', 'tipo', 'internacional')
    # Asegúrate de que 'fields' o 'fieldsets' también usen 'imagen_estatica'
    fields = ['nombre', 'tipo', 'fecha', 'ubicacion', 'descripcion', 'internacional', 'imagen_estatica']

    def imagen_estatica_display(self, obj):
        # Muestra una previsualización de la imagen estática en el admin listado
        if obj.imagen_estatica:
            # La ruta asume que la imagen está en tu carpeta 'static/'
            # Por ejemplo, si el campo tiene 'images/mi_torneo.png', se convertirá en /static/images/mi_torneo.png
            return format_html('<img src="/static/{}" style="width: 50px; height: auto;" />', obj.imagen_estatica)
        return "(Sin imagen)"
    imagen_estatica_display.short_description = 'Imagen'


# Clase para personalizar la visualización de InformacionTorneoAnio en el admin
@admin.register(InformacionTorneoAnio)
class InformacionTorneoAnioAdmin(admin.ModelAdmin):
    # Asegúrate de que list_display usa los nuevos nombres de campo y el método de previsualización
    list_display = ('torneo', 'anio', 'campeon', 'participantes_cantidad', 'link_transmision', 'imagen_edicion_estatica_display') 
    search_fields = ('torneo__nombre', 'anio', 'campeon')
    list_filter = ('anio', 'torneo')
    # Asegúrate de que 'fields' o 'fieldsets' también usen 'imagen_edicion_estatica'
    fields = [
        'torneo', 'anio', 'campeon', 'subcampeon', 'participantes_cantidad',
        'resumen', 'link_transmision', 'fecha_exacta', 'ubicacion_especifica', 'imagen_edicion_estatica'
    ]

    def imagen_edicion_estatica_display(self, obj):
        # Muestra una previsualización de la imagen estática de la edición en el admin listado
        if obj.imagen_edicion_estatica:
            return format_html('<img src="/static/{}" style="width: 50px; height: auto;" />', obj.imagen_edicion_estatica)
        return "(Sin imagen)"
    imagen_edicion_estatica_display.short_description = 'Imagen Edición'


# Clase para personalizar la visualización de ImagenCarrusel en el admin
@admin.register(ImagenCarrusel)
class ImagenCarruselAdmin(admin.ModelAdmin):
    # Asegúrate de usar 'imagen_estatica' y su método de visualización
    list_display = ('titulo', 'orden', 'activo', 'imagen_preview', 'fecha_subida')
    list_editable = ('orden', 'activo')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('activo',)
    readonly_fields = ('imagen_preview', 'fecha_subida') 
    # Asegúrate de que 'fields' o 'fieldsets' también usen 'imagen_estatica'
    fields = ('titulo', 'imagen_estatica', 'descripcion', 'orden', 'activo', 'fecha_subida')

    # La función imagen_preview ahora está en el modelo ImagenCarrusel y usa la ruta estática
    # No necesitas definirla aquí si ya está en el modelo y usa format_html.
    # Si la tuvieras definida aquí, sería similar a imagen_estatica_display.

