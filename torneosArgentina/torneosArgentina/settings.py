import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# =======================================================================
# SEGURIDAD Y HOSTS PERMITIDOS
# =======================================================================
# SECRET_KEY: ¡MUY IMPORTANTE! Usa una variable de entorno en producción.
# NUNCA expongas tu SECRET_KEY directamente en el código.
# En GitLab CI/CD la configurarás como una variable de CI/CD.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'tu-clave-secreta-de-desarrollo-aqui-si-quieres')

# DEBUG: Siempre False en producción.
DEBUG = os.environ.get('DJANGO_DEBUG', 'False').lower() == 'true'

# ALLOWED_HOSTS: Permite los dominios donde se desplegará tu aplicación.
# En GitLab CI/CD, esto puede ser el dominio de tu servicio de hosting.
# Para Render/Heroku, suelen inyectar un hostname.
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')
if not DEBUG:
    # Asegúrate de que ALLOWED_HOSTS no esté vacío en producción.
    # Si usas Render, Render automáticamente inyecta RENDER_EXTERNAL_HOSTNAME.
    # Puedes añadirlo aquí si lo necesitas para otras plataformas.
    pass

# =======================================================================
# BASE DE DATOS
# =======================================================================
# Para producción, es ALTAMENTE RECOMENDADO usar PostgreSQL o MySQL.
# Las credenciales deben venir de variables de entorno.
# Si sigues con SQLite, el archivo de la base de datos estará en tu repo,
# lo cual NO es ideal para producción (no es escalable ni persistente).
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Puedes mantener SQLite para simplicidad inicial
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Ejemplo para PostgreSQL (si decides usarlo más adelante):
# import dj_database_url
# DATABASE_URL = os.environ.get('DATABASE_URL')
# if DATABASE_URL:
#     DATABASES['default'] = dj_database_url.parse(DATABASE_URL)


# =======================================================================
# ARCHIVOS ESTÁTICOS Y MEDIA
# =======================================================================
# Instala 'whitenoise' (pip install whitenoise) para servir archivos estáticos en producción.
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Donde Django recolectará los estáticos

# Directorios donde Django buscará archivos estáticos (en desarrollo)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "Torneos", "static"), # Ajusta si tu app se llama diferente
]

# Configuración de WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (archivos subidos por usuarios, como imágenes de torneos)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# En producción, MEDIA_ROOT debería ser un servicio de almacenamiento de objetos (AWS S3, Google Cloud Storage)
# usando librerías como django-storages, ya que los archivos en el servidor pueden perderse en cada despliegue.

# =======================================================================
# MIDDLEWARE
# =======================================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # <-- ¡Asegúrate de que esté aquí!
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ... el resto de tu settings.py
