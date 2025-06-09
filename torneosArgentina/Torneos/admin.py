from django.contrib import admin
from django.utils.html import format_html
from .models import Torneo, ImagenCarrusel, InformacionTorneoAnio, ImagenAdicionalTorneo # Importa el nuevo modelo

# ===========================================================================
# INLINE para InformacionTorneoAnio
# Permite agregar y editar ediciones anuales directamente desde el formulario de Torneo.
# ===========================================================================
class InformacionTorneoAnioInline(admin.TabularInline):
    model = InformacionTorneoAnio
    extra = 1
    fields = [
        'anio', 'campeon', 'subcampeon', 'participantes_cantidad',
        'resumen', 'link_transmision', 'fecha_exacta', 'ubicacion_especifica',
        'imagen_edicion_estatica'
    ]

# ===========================================================================
# NUEVO INLINE: ImagenAdicionalTorneoInline
# Permite agregar múltiples imágenes a un Torneo desde su formulario de edición.
# ===========================================================================
class ImagenAdicionalTorneoInline(admin.TabularInline): # O admin.StackedInline para una vista más expansiva
    model = ImagenAdicionalTorneo
    extra = 1 # Cuántos formularios vacíos se muestran por defecto
    fields = ['imagen_estatica', 'descripcion', 'orden']
    # Opcional: para mostrar una previsualización en el admin
    readonly_fields = ['imagen_preview_admin']

    def imagen_preview_admin(self, obj):
        if obj.imagen_estatica:
            return format_html('<img src="/static/{}" style="width: 80px; height: auto;" />', obj.imagen_estatica)
        return "(Sin imagen)"
    imagen_preview_admin.short_description = 'Previsualización'


# ===========================================================================
# Admin para el modelo Torneo (Torneos Principales)
# ===========================================================================
@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'tipo', 'ubicacion', 'internacional', 'imagen_estatica_display') 
    search_fields = ('nombre', 'tipo', 'ubicacion')
    list_filter = ('fecha', 'tipo', 'internacional')
    fields = ['nombre', 'tipo', 'fecha', 'ubicacion', 'descripcion', 'internacional', 'imagen_estatica']

    # ¡IMPORTANTE: Agrega el nuevo Inline aquí!
    inlines = [InformacionTorneoAnioInline, ImagenAdicionalTorneoInline]

    def imagen_estatica_display(self, obj):
        if obj.imagen_estatica:
            return format_html('<img src="/static/{}" style="width: 50px; height: auto;" />', obj.imagen_estatica)
        return "(Sin imagen)"
    imagen_estatica_display.short_description = 'Imagen Principal'


# ===========================================================================
# Admin para el modelo InformacionTorneoAnio
# ===========================================================================
@admin.register(InformacionTorneoAnio)
class InformacionTorneoAnioAdmin(admin.ModelAdmin):
    list_display = ('torneo', 'anio', 'campeon', 'participantes_cantidad', 'link_transmision', 'imagen_edicion_estatica_display') 
    search_fields = ('torneo__nombre', 'anio', 'campeon')
    list_filter = ('anio', 'torneo')
    fields = [
        'torneo', 'anio', 'campeon', 'subcampeon', 'participantes_cantidad',
        'resumen', 'link_transmision', 'fecha_exacta', 'ubicacion_especifica', 'imagen_edicion_estatica'
    ]

    def imagen_edicion_estatica_display(self, obj):
        if obj.imagen_edicion_estatica:
            return format_html('<img src="/static/{}" style="width: 50px; height: auto;" />', obj.imagen_edicion_estatica)
        return "(Sin imagen)"
    imagen_edicion_estatica_display.short_description = 'Imagen Edición'


# ===========================================================================
# Admin para el modelo ImagenCarrusel
# (No se modifica para esta funcionalidad)
# ===========================================================================
@admin.register(ImagenCarrusel)
class ImagenCarruselAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'activo', 'imagen_preview', 'fecha_subida')
    list_editable = ('orden', 'activo')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('activo',)
    readonly_fields = ('imagen_preview', 'fecha_subida') 
    fields = ('titulo', 'imagen_estatica', 'descripcion', 'orden', 'activo', 'fecha_subida')

