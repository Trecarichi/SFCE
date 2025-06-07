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
    "whitenoise.middleware.WhiteHouseMiddleware", # <-- Corregido a WhiteNoiseMiddleware si era un typo
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
# Primero, obtenemos la URL de la base de datos de la variable de entorno
database_url = os.environ.get('DATABASE_URL')

# Si la variable de entorno DATABASE_URL existe Y NO ESTÁ VACÍA
if database_url:
    DATABASES = {
        'default': dj_database_url.config(default=database_url)
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
# ARCHIVOS MEDIA (¡Ya no son relevantes si todas las imágenes son estáticas!)
# =======================================================================
# Dado que todas las imágenes de los modelos ahora son CharField y se gestionan como estáticas,
# estas configuraciones de MEDIA_URL y MEDIA_ROOT son menos críticas.
# Se mantienen solo por si Django las necesita para otras funcionalidades internas.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
