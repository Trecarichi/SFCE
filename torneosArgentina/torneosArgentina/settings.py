import os
from pathlib import Path
import dj_database_url # <--- Asegúrate de que esto esté aquí

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'tu-clave-secreta-de-desarrollo-aqui-si-quieres')
DEBUG = False # Siempre False en producción

allowed_hosts_from_env = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')
allowed_hosts_from_env = [host.strip() for host in allowed_hosts_from_env if host.strip()]
render_hostname = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if render_hostname and render_hostname not in allowed_hosts_from_env:
    allowed_hosts_from_env.append(render_hostname)
ALLOWED_HOSTS = allowed_hosts_from_env

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Torneos", # Tu aplicación de torneos
    "torneosArgentina", # Tu aplicación principal
]

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

ROOT_URLCONFE = "torneosArgentina.urls"

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
                "django.template.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "torneosArgentina.wsgi.application"

# =======================================================================
# BASE DE DATOS (¡CONFIGURACIÓN PARA POSTGRESQL - AHORA ACTIVA!)
# =======================================================================
# Si la variable de entorno DATABASE_URL existe (provista por Render PostgreSQL)
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600) # Usar dj_database_url para parsear la URL de Render
    }
else: # Si no, usa SQLite localmente (para desarrollo)
    DATABASES = {
        'default': {
            'ENGINE': "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

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

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "Torneos", "static"),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
