# Torneos/admin.py

from django.contrib import admin
from .models import Torneo, InformacionTorneoAnio, ImagenCarrusel, ImagenTorneo

# Inline para InformacionTorneoAnio para que se pueda agregar/editar directamente desde el Torneo
class InformacionTorneoAnioInline(admin.TabularInline):
    model = InformacionTorneoAnio
    extra = 1 # Cuántos formularios vacíos se muestran por defecto


# INLINE PARA IMAGENESTORNEO
class ImagenTorneoInline(admin.TabularInline):
    model = ImagenTorneo
    extra = 1 # Cuántos formularios vacíos se muestran por defecto
    fields = ['imagen_estatica_adicional', 'descripcion', 'orden', 'imagen_preview'] # Muestra los campos en el admin
    readonly_fields = ['imagen_preview'] # Hace que la previsualización sea de solo lectura


@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'fecha', 'ubicacion', 'internacional', 'imagen_preview')
    list_filter = ('tipo', 'internacional', 'fecha')
    search_fields = ('nombre', 'descripcion', 'ubicacion')
    ordering = ('-fecha',) # Ordenar por fecha descendente

    # Inlines para poder agregar InformacionTorneoAnio e ImagenTorneo desde el detalle del Torneo
    inlines = [InformacionTorneoAnioInline, ImagenTorneoInline] # Ya tenías ImagenTorneoInline aquí

    # Mostrar previsualización de la imagen principal en la lista de torneos
    def imagen_preview(self, obj):
        from django.utils.html import mark_safe
        from django.templatetags.static import static
        if obj.imagen_estatica:
            return mark_safe(f'<img src="{static(obj.imagen_estatica)}" style="width: 50px; height: auto;" />')
        return ""
    imagen_preview.short_description = 'Imagen Principal'


@admin.register(ImagenCarrusel)
class ImagenCarruselAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden', 'activo', 'fecha_subida', 'imagen_preview')
    list_filter = ('activo',)
    search_fields = ('titulo', 'descripcion')
    ordering = ('orden',)
    fields = ('titulo', 'imagen_estatica', 'descripcion', 'orden', 'activo', 'fecha_subida', 'imagen_preview')
    readonly_fields = ('fecha_subida', 'imagen_preview') # fecha_subida es auto_now_add

    # Ya tienes el método imagen_preview en el modelo, el admin.ModelAdmin ya lo usa


# REGISTRAR EXPLICITAMENTE INFORMACIONTORNEOANIO EN EL ADMIN
# Esto es necesario incluso si también se usa como Inline, para evitar el error 500
@admin.register(InformacionTorneoAnio)
class InformacionTorneoAnioAdmin(admin.ModelAdmin):
    list_display = ('torneo', 'anio', 'campeon', 'subcampeon')
    list_filter = ('anio', 'torneo')
    search_fields = ('torneo__nombre', 'campeon', 'subcampeon')
    ordering = ('-anio',) # Ordenar por año descendente
