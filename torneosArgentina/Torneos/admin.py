from django.contrib import admin
from django.utils.html import format_html
# Asegúrate de importar todos los modelos necesarios
from .models import Torneo, ImagenCarrusel, InformacionTorneoAnio, ImagenAdicionalTorneo

# ===========================================================================
# INLINE para InformacionTorneoAnio
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
# INLINE: ImagenAdicionalTorneoInline
# ===========================================================================
class ImagenAdicionalTorneoInline(admin.TabularInline):
    model = ImagenAdicionalTorneo
    extra = 1
    fields = ['imagen_estatica', 'descripcion', 'orden']
    readonly_fields = ['imagen_preview_admin']

    def imagen_preview_admin(self, obj):
        from django.templatetags.static import static # Importar static aquí si es necesario
        if obj.imagen_estatica:
            return format_html('<img src="{}" style="width: 80px; height: auto;" />', static(obj.imagen_estatica))
        return "(Sin imagen)"
    imagen_preview_admin.short_description = 'Previsualización'


# ===========================================================================
# Admin para el modelo Torneo (Torneos Principales)
# ===========================================================================
@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
    # CAMBIO: 'internacional' a 'es_offline' en list_display
    list_display = ('nombre', 'fecha', 'tipo', 'ubicacion', 'es_offline', 'imagen_estatica_display') 
    search_fields = ('nombre', 'tipo', 'ubicacion')
    # CAMBIO: 'internacional' a 'es_offline' en list_filter
    list_filter = ('fecha', 'tipo', 'es_offline')
    # CAMBIO: 'internacional' a 'es_offline' en fields
    fields = ['nombre', 'tipo', 'fecha', 'ubicacion', 'descripcion', 'es_offline', 'imagen_estatica']
    inlines = [InformacionTorneoAnioInline, ImagenAdicionalTorneoInline] # Asegúrate de que ImagenAdicionalTorneoInline esté aquí

    def imagen_estatica_display(self, obj):
        from django.templatetags.static import static # Importar static aquí si es necesario
        if obj.imagen_estatica:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', static(obj.imagen_estatica))
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
        from django.templatetags.static import static # Importar static aquí si es necesario
        if obj.imagen_edicion_estatica:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', static(obj.imagen_edicion_estatica))
        return "(Sin imagen)"
    imagen_edicion_estatica_display.short_description = 'Imagen Edición'


# ===========================================================================
# Admin para el modelo ImagenCarrusel
# ===========================================================================
@admin.register(ImagenCarrusel)
class ImagenCarruselAdmin(admin.ModelAdmin):
    # Asegúrate de que 'imagen_preview' es el nombre del método en el modelo
    list_display = ('titulo', 'orden', 'activo', 'imagen_preview', 'fecha_subida')
    list_editable = ('orden', 'activo') # Permite editar orden y activo directamente en la lista
    search_fields = ('titulo', 'descripcion')
    list_filter = ('activo',)
    readonly_fields = ('imagen_preview', 'fecha_subida') 
    # Asegúrate de que 'imagen_estatica' es el campo aquí y no 'imagen'
    fields = ('titulo', 'imagen_estatica', 'descripcion', 'orden', 'activo', 'fecha_subida')
