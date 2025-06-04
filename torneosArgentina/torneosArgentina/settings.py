from pathlib import Path
import os

# Determina la ruta base del proyecto.
# Para PythonAnywhere, BASE_DIR debe apuntar a la carpeta que contiene manage.py
# Si tu estructura es /home/tu_usuario/SFCE/torneosArgentina/manage.py
# y settings.py está en /home/tu_usuario/SFCE/torneosArgentina/torneosArgentina/settings.py
# entonces Path(__file__).resolve().parent.parent es la carpeta 'torneosArgentina'
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+o(1nsm_h!8oaxig*s3o5w7tp!^vz0t5n)tp6d*8dz5^_$-war"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False # <-- ¡MUY IMPORTANTE: CAMBIAR A FALSE PARA PRODUCCIÓN!

# Añade el dominio de tu sitio en PythonAnywhere
ALLOWED_HOSTS = ['sfceargentina.pythonanywhere.com'] # <-- ¡Asegúrate que este sea tu dominio real!

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Torneos",
    "torneosArgentina",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
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
        "DIRS": [os.path.join(BASE_DIR, "Torneos", "templates")], # Ajusta esta ruta si tus templates están en otro lugar
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

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

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

# Configuración de archivos estáticos para producción
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # <-- Aquí se recolectarán todos los archivos estáticos

# Directorios donde Django buscará archivos estáticos durante el desarrollo (opcional para producción)
# Si tus archivos estáticos están en Torneos/static/, esta es la ruta correcta
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "Torneos", "static"),
]

# Media files (para archivos subidos por usuarios, como imágenes de torneos)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
