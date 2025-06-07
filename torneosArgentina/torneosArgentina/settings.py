import os
from pathlib import Path
import dj_database_url # Importar dj_database_url

# Determina la ruta base del proyecto.
# Asume que manage.py está en la carpeta 'torneosArgentina',
# y settings.py está en 'torneosArgentina/torneosArgentina/settings.py'.
# Entonces, BASE_DIR debe apuntar a la carpeta 'torneosArgentina' (donde está manage.py).
BASE_DIR = Path(__file__).resolve().parent.parent

# =======================================================================
# SEGURIDAD Y HOSTS PERMITIDOS (¡CRÍTICO PARA PRODUCCIÓN!)
# =======================================================================
# Utiliza una variable de entorno para SECRET_KEY.
# En Render, esto se configura en 'Environment'.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'tu-clave-secreta-de-desarrollo-aqui-si-quieres')

# DEBUG debe ser False en producción por seguridad.
# Render también puede inyectar esto vía 'DJANGO_DEBUG' environment variable.
DEBUG = False

# Configura los hosts permitidos.
# Render inyecta 'RENDER_EXTERNAL_HOSTNAME' automáticamente.
# También puedes definir 'DJANGO_ALLOWED_HOSTS' en las variables de entorno de Render,
# con dominios separados por comas (ej. 'mi-dominio.com,www.mi-dominio.com').
allowed_hosts_from_env = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')
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
    "django.contrib.messages", # ¡Asegúrate de que esta línea esté presente!
    "django.contrib.staticfiles",
    "Torneos", # Tu aplicación de torneos
    "torneosArgentina", # Tu aplicación principal
    # 'storages', # Descomenta si decides usar AWS S3 en el futuro para media files
]

# =======================================================================
# MIDDLEWARE
# =======================================================================
# WhiteNoise debe ir justo después de SecurityMiddleware para servir estáticos.
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

# =======================================================================
# CONFIGURACIÓN DE TEMPLATES (¡CRÍTICO PARA EL ADMIN!)
# =======================================================================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Define dónde Django buscará tus templates.
        # Asumiendo que tus templates están en 'tu_proyecto_django/Torneos/template/'.
        # Es decir, la carpeta 'template' (singular) dentro de la app 'Torneos'.
        "DIRS": [os.path.join(BASE_DIR, "Torneos", "template")],
        "APP_DIRS": True, # Permite a Django buscar templates en las carpetas 'templates' de cada app.
                          # Aunque 'DIRS' apunta explícitamente, 'APP_DIRS' es útil para templates de apps de Django.
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages", # <--- ¡ESTA LÍNEA DEBE ESTAR SÍ O SÍ!
            ],
        },
    },
]

WSGI_APPLICATION = "torneosArgentina.wsgi.application"

# =======================================================================
# BASE DE DATOS (¡CONFIGURACIÓN PARA POSTGRESQL O SQLITE!)
# =======================================================================
# Si la variable de entorno DATABASE_URL existe (provista por Render para PostgreSQL)
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
    }
else: # Si no, usa SQLite localmente (para desarrollo)
    DATABASES = {
        'default': {
            'ENGINE': "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
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
    os.path.join(BASE_DIR, "Torneos", "static"), # Ruta a la carpeta 'static' de tu app 'Torneos'
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# =======================================================================
# ARCHIVOS MEDIA (Para archivos subidos por el usuario, si los hay)
# =======================================================================
# Si todos tus campos de imagen en los modelos son CharField (para estáticas),
# esta sección es menos crítica, pero es buena práctica tenerla.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
