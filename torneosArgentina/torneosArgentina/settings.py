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
# ¡IMPORTANTE! Lo hemos vuelto a poner en False para producción.
DEBUG = True # os.environ.get('DJANGO_DEBUG', 'False').lower() == 'true'

# ALLOWED_HOSTS: Permite los dominios donde se desplegará tu aplicación.
# Esta lógica es más robusta para manejar RENDER_EXTERNAL_HOSTNAME y DJANGO_ALLOWED_HOSTS.
allowed_hosts_from_env = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')
# Limpia las cadenas vacías que pueden resultar de un split de una cadena vacía o comas al final
allowed_hosts_from_env = [host.strip() for host in allowed_hosts_from_env if host.strip()]

render_hostname = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if render_hostname and render_hostname not in allowed_hosts_from_env:
    allowed_hosts_from_env.append(render_hostname)

ALLOWED_HOSTS = allowed_hosts_from_env

# --- DEBUGGING PRINTS ---
# Estas líneas de depuración ya no son necesarias en producción, pero las mantengo comentadas
# por si las necesitas en el futuro. En producción, los logs detallados no deben ser públicos.
# print(f"DEBUG: Final DEBUG value: {DEBUG}")
# print(f"DEBUG: Final ALLOWED_HOSTS value: {ALLOWED_HOSTS}")
# print(f"DEBUG: RENDER_EXTERNAL_HOSTNAME: {os.environ.get('RENDER_EXTERNAL_HOSTNAME')}")
# --- END DEBUGGING PRINTS ---

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
        # Ruta a la carpeta 'template' (singular) dentro de la app 'Torneos'
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
