# torneosArgentina/urls.py (¡Este es el archivo principal de tu proyecto!)

from django.contrib import admin
from django.urls import path, include

# Importa settings y static para servir MEDIA y STATIC en desarrollo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ¡ESTA LÍNEA ES LA QUE FALTA Y ES CRUCIAL PARA EL ADMIN!
    path('admin/', admin.site.urls),

    # Esta línea incluye las URLs de tu aplicación Torneos
    # Asegúrate de que el nombre 'Torneos' sea el nombre exacto de tu aplicación
    path('', include('Torneos.urls')),
]

# Estas líneas sirven los archivos de medios (tus imágenes subidas) y estáticos (CSS, JS)
# en modo de desarrollo (cuando DEBUG = True).
# ¡RECUERDA ELIMINAR ESTAS LÍNEAS CUANDO DESPLIEGUES A UN ENTORNO DE PRODUCCIÓN!
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)