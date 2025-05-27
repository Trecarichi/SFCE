# Torneos/admin.py

from django.contrib import admin
from .models import Torneo, ImagenCarrusel, InformacionTorneoAnio

# Personaliza cómo se muestran los Torneos en el admin
class TorneoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'fecha', 'ubicacion', 'internacional', 'imagen_preview')
    list_filter = ('tipo', 'internacional', 'fecha')
    search_fields = ('nombre', 'ubicacion', 'descripcion')
    date_hierarchy = 'fecha'
    fields = ('nombre', 'tipo', 'fecha', 'ubicacion', 'descripcion', 'internacional', 'imagen_torneo')
    readonly_fields = ('imagen_preview',)

    def imagen_preview(self, obj):
        if obj.imagen_torneo:
            from django.utils.html import mark_safe
            return mark_safe(f'<img src="{obj.imagen_torneo.url}" style="width: 80px; height: auto; border-radius: 4px;" />')
        return "(Sin imagen)"
    imagen_preview.short_description = 'Imagen'

# Personaliza cómo se muestran las Imágenes de Carrusel
class ImagenCarruselAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'activo', 'fecha_subida', 'imagen_preview')
    list_filter = ('activo',)
    search_fields = ('titulo', 'descripcion')
    list_editable = ('orden', 'activo',)

    def imagen_preview(self, obj):
        if obj.imagen:
            from django.utils.html import mark_safe
            return mark_safe(f'<img src="{obj.imagen.url}" style="width: 50px; height: auto;" />')
        return ""
    imagen_preview.short_description = 'Previsualización'

# Personaliza cómo se muestran las Informaciones de Torneo por Año
class InformacionTorneoAnioAdmin(admin.ModelAdmin):
    list_display = ('torneo', 'anio', 'fecha_exacta', 'ubicacion_especifica', 'campeon', 'subcampeon', 'participantes_cantidad', 'link_transmision_display') # Agregados
    list_filter = ('anio', 'torneo__nombre')
    search_fields = ('torneo__nombre', 'campeon', 'subcampeon', 'resumen', 'link_transmision') # Agregado 'link_transmision'
    raw_id_fields = ('torneo',) # Útil para seleccionar el Torneo si hay muchos

    # Para que el link de transmisión sea clickeable en la lista del admin
    def link_transmision_display(self, obj):
        if obj.link_transmision:
            from django.utils.html import format_html
            return format_html('<a href="{}" target="_blank">Ver Transmisión</a>', obj.link_transmision)
        return ""
    link_transmision_display.short_description = 'Transmisión'

# Registra tus modelos con sus personalizaciones
admin.site.register(Torneo, TorneoAdmin)
admin.site.register(ImagenCarrusel, ImagenCarruselAdmin)
admin.site.register(InformacionTorneoAnio, InformacionTorneoAnioAdmin)