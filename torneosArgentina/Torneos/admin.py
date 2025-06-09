from django.contrib import admin
from django.utils.html import format_html # Importa format_html
from .models import Torneo, ImagenCarrusel, InformacionTorneoAnio

# ===========================================================================
# INLINE para InformacionTorneoAnio
# Permite agregar y editar ediciones anuales directamente desde el formulario de Torneo.
# ===========================================================================
class InformacionTorneoAnioInline(admin.TabularInline):
    model = InformacionTorneoAnio
    extra = 1 # Cuántos formularios vacíos se muestran por defecto
    # Asegúrate de que los campos aquí coincidan con el modelo y sean CharField si son estáticos
    fields = [
        'anio', 'campeon', 'subcampeon', 'participantes_cantidad',
        'resumen', 'link_transmision', 'fecha_exacta', 'ubicacion_especifica',
        'imagen_edicion_estatica' # <-- Campo de imagen estática para la edición anual
    ]
    # Si quieres una previsualización en el inline (más avanzado, podría requerir un custom form/widget)
    # No lo agregamos por defecto aquí para evitar complicaciones.
    # Si lo agregaras, deberías añadir 'readonly_fields' y un método `imagen_edicion_estatica_preview` similar al de TorneoAdmin.


# ===========================================================================
# Admin para el modelo Torneo (Torneos Principales)
# ===========================================================================
@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista del admin
    list_display = ('nombre', 'fecha', 'tipo', 'ubicacion', 'internacional', 'imagen_estatica_display') 
    
    # Campos para búsqueda y filtro
    search_fields = ('nombre', 'tipo', 'ubicacion')
    list_filter = ('fecha', 'tipo', 'internacional')
    
    # Campos a mostrar y editar en el formulario de detalle del torneo
    fields = ['nombre', 'tipo', 'fecha', 'ubicacion', 'descripcion', 'internacional', 'imagen_estatica']

    # Inlines para agregar a la vista de detalle del Torneo
    # ¡CRÍTICO: Solo incluimos inlines que correspondan a modelos existentes!
    inlines = [InformacionTorneoAnioInline] # <-- Asegúrate de que ImagenTorneoInline NO esté aquí si no existe el modelo

    # Método para mostrar la previsualización de la imagen estática del torneo en el listado
    def imagen_estatica_display(self, obj):
        if obj.imagen_estatica:
            # La ruta asume que la imagen está en tu carpeta 'static/'
            # Por ejemplo, si el campo tiene 'images/mi_torneo.png', se convertirá en /static/images/mi_torneo.png
            return format_html('<img src="/static/{}" style="width: 50px; height: auto;" />', obj.imagen_estatica)
        return "(Sin imagen)"
    imagen_estatica_display.short_description = 'Imagen Principal'


# ===========================================================================
# Admin para el modelo InformacionTorneoAnio
# (Aunque se usa como Inline, se registra por separado para gestión directa)
# ===========================================================================
@admin.register(InformacionTorneoAnio)
class InformacionTorneoAnioAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista del admin
    list_display = ('torneo', 'anio', 'campeon', 'participantes_cantidad', 'link_transmision', 'imagen_edicion_estatica_display') 
    
    # Campos para búsqueda y filtro
    search_fields = ('torneo__nombre', 'anio', 'campeon')
    list_filter = ('anio', 'torneo')
    
    # Campos a mostrar y editar en el formulario de detalle de la edición anual
    fields = [
        'torneo', 'anio', 'campeon', 'subcampeon', 'participantes_cantidad',
        'resumen', 'link_transmision', 'fecha_exacta', 'ubicacion_especifica', 'imagen_edicion_estatica'
    ]

    # Método para mostrar la previsualización de la imagen estática de la edición en el listado
    def imagen_edicion_estatica_display(self, obj):
        if obj.imagen_edicion_estatica:
            return format_html('<img src="/static/{}" style="width: 50px; height: auto;" />', obj.imagen_edicion_estatica)
        return "(Sin imagen)"
    imagen_edicion_estatica_display.short_description = 'Imagen Edición'


# ===========================================================================
# Admin para el modelo ImagenCarrusel
# (Asegúrate de que este modelo también use imagen_estatica si así lo decidiste)
# ===========================================================================
@admin.register(ImagenCarrusel)
class ImagenCarruselAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista del admin
    # 'imagen_preview' es un método del modelo ImagenCarrusel (si lo tienes) que usa 'imagen_estatica'
    list_display = ('titulo', 'orden', 'activo', 'imagen_preview', 'fecha_subida')
    
    # Campos editables directamente desde la lista (opcional)
    list_editable = ('orden', 'activo')
    
    # Campos para búsqueda y filtro
    search_fields = ('titulo', 'descripcion')
    list_filter = ('activo',)
    
    # Campos de solo lectura (como la previsualización de la imagen y la fecha de subida)
    readonly_fields = ('imagen_preview', 'fecha_subida') 
    
    # Campos a mostrar y editar en el formulario de detalle de la imagen del carrusel
    # ¡CRÍTICO: Asegúrate de que 'imagen_estatica' sea el campo aquí!
    fields = ('titulo', 'imagen_estatica', 'descripcion', 'orden', 'activo', 'fecha_subida')

    # El método `imagen_preview` se define en el modelo `ImagenCarrusel` y ya está adaptado
    # para usar `self.imagen_estatica`. No necesitas redefinirlo aquí.

