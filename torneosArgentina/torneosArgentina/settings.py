import os
from pathlib import Path

# Determina la ruta base del proyecto.
# Si settings.py está en 'SFCE/torneosArgentina/torneosArgentina/settings.py',
# y tu manage.py está en 'SFCE/torneosArgentina/',
# entonces Path(__file__).resolve().parent.parent es la carpeta 'torneosArgentina'
# (donde está manage.py).
BASE_DIR = Path(__file__).resolve().parent.parent

# =======================================================================
# SEGURIDAD Y HOSTS PERMITIDOS (¡CRÍTICO PARA PRODUCCIÓN!)
# =======================================================================
# SECRET_KEY: ¡MUY IMPORTANTE! Usa una variable de entorno en producción.
# NUNCA expongas tu SECRET_KEY directamente en el código.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'tu-clave-secreta-de-desarrollo-aqui-si-quieres')

# DEBUG: Siempre False en producción.
# Render inyectará 'False' si configuras DJANGO_DEBUG=False en sus variables de entorno.
DEBUG = os.environ.get('DJANGO_DEBUG', 'False').lower() == 'true'

# ALLOWED_HOSTS: Permite los dominios donde se desplegará tu aplicación.
# Render inyecta RENDER_EXTERNAL_HOSTNAME automáticamente.
# También puedes definir DJANGO_ALLOWED_HOSTS en las variables de entorno de Render
# para incluir dominios personalizados, separados por comas.
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')
# Si no hay DJANGO_ALLOWED_HOSTS, Render automáticamente inyecta RENDER_EXTERNAL_HOSTNAME.
# Asegúrate de que RENDER_EXTERNAL_HOSTNAME esté incluido si no usas DJANGO_ALLOWED_HOSTS.
if not ALLOWED_HOSTS and os.environ.get('RENDER_EXTERNAL_HOSTNAME'):
    ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_HOSTNAME')]

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
]

# =======================================================================
# MIDDLEWARE (¡Añadir WhiteNoise aquí!)
# =======================================================================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # WhiteNoise debe ir justo después de SecurityMiddleware
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
        # Ruta a la carpeta 'templates' dentro de la app 'Torneos'
        "DIRS": [os.path.join(BASE_DIR, "Torneos", "templates")],
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
# BASE DE DATOS
# =======================================================================
# Render inyecta las variables de entorno para PostgreSQL (DB_NAME, DB_USER, etc.)
# Si usas SQLite, asegúrate de que el archivo db.sqlite3 no esté en .gitignore para producción.
# Para producción, se recomienda PostgreSQL.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Mantener SQLite para simplicidad inicial
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Si usas PostgreSQL de Render, puedes descomentar y usar dj_database_url:
# import dj_database_url
# DATABASE_URL = os.environ.get('DATABASE_URL')
# if DATABASE_URL:
#     DATABASES['default'] = dj_database_url.parse(DATABASE_URL)


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# =======================================================================
# ARCHIVOS ESTÁTICOS Y MEDIA (¡Configuración de WhiteNoise!)
# =======================================================================
STATIC_URL = '/static/'
# STATIC_ROOT es donde 'collectstatic' copiará todos tus archivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_DIRS es donde Django buscará tus archivos estáticos durante el desarrollo
# y donde 'collectstatic' los encontrará para copiarlos a STATIC_ROOT.
# Si tus archivos estáticos están en 'Torneos/static/', esta es la ruta correcta.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "Torneos", "static"),
]

# Configuración de WhiteNoise para servir archivos estáticos comprimidos y con caché
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (para archivos subidos por usuarios, como imágenes de torneos)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # Aquí se guardarán las imágenes subidas


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
