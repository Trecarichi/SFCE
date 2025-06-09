import os
from pathlib import Path
import dj_database_url # Importar dj_database_url

# Determina la ruta base del proyecto.
BASE_DIR = Path(__file__).resolve().parent.parent

# =======================================================================
# SEGURIDAD Y HOSTS PERMITIDOS (¡CRÍTICO PARA PRODUCCIÓN!)
# =======================================================================
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'tu-clave-secreta-de-desarrollo-aqui-si-quieres')
DEBUG = False # ¡DEBUG debe ser False en producción por seguridad!

# Primero, define allowed_hosts_from_env desde las variables de entorno
allowed_hosts_from_env = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')
# Luego, refina la lista (esto ya opera sobre la variable definida)
allowed_hosts_from_env = [host.strip() for host in allowed_hosts_from_env if host.strip()]

render_hostname = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if render_hostname and render_hostname not in allowed_hosts_from_env:
    allowed_hosts_from_env.append(render_hostname)
ALLOWED_HOSTS = allowed_hosts_from_env

# =======================================================================
# APLICACIONES INSTALADAS
# =======================================================================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Torneos", # Tu aplicación de torneos
    "torneosArgentina", # Tu aplicación principal
    # 'storages', # Descomenta si decides usar AWS S3 en el futuro para media files
]

# =======================================================================
# MIDDLEWARE
# =======================================================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "torneosArgentina.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "Torneos", "template")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "torneosArgentina.wsgi.application"

# =======================================================================
# BASE DE DATOS (¡CONFIGURACIÓN PARA POSTGRESQL!)
# =======================================================================
# Si la variable de entorno DATABASE_URL existe (provista por Render PostgreSQL)
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
    }
else: # Si no, usa SQLite localmente (para desarrollo)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    
# Password validation
AUTH_PASSWORD_VALIDATORS = [
    { "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator", },
    { "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    { "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    { "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# =======================================================================
# ARCHIVOS ESTÁTICOS
# =======================================================================
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "Torneos", "static"),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# =======================================================================
# ARCHIVOS MEDIA (Imágenes subidas por el admin - ¡Ahora serán persistentes si configuras S3!)
# =======================================================================
# Estas líneas son para archivos media que se suben por el admin (como el modelo ImagenCarrusel si no lo cambiaste a static).
# Si estás usando ImageField y *quieres que persistan*, necesitas configurar django-storages con AWS S3.
# Si estás usando CharField para las rutas de imagen estática (como acordamos),
# entonces MEDIA_URL y MEDIA_ROOT son menos críticos para esas imágenes,
# pero aún pueden ser necesarios para otras funcionalidades de Django.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
