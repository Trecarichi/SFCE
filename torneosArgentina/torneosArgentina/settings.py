from pathlib import Path
import os

# Determina la ruta base del proyecto.
# Si settings.py está en 'SFCE/torneosArgentina/torneosArgentina/settings.py',
# entonces Path(__file__).resolve() es .../SFCE/torneosArgentina/torneosArgentina/settings.py
# .parent es .../SFCE/torneosArgentina/torneosArgentina/
# .parent.parent es .../SFCE/torneosArgentina/ (¡Esta es la raíz del proyecto, donde está manage.py!)
BASE_DIR = Path(__file__).resolve().parent.parent

# --- DEBUGGING PRINTS ---
print(f"DEBUG: BASE_DIR in settings.py: {BASE_DIR}")
print(f"DEBUG: DJANGO_SETTINGS_MODULE env var: {os.environ.get('DJANGO_SETTINGS_MODULE')}")
# --- END DEBUGGING PRINTS ---

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+o(1nsm_h!8oaxig*s3o5w7tp!^vz0t5n)tp6d*8dz5^_$-war"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # ¡Correcto para desarrollo local!

ALLOWED_HOSTS = [] # Correcto para desarrollo local

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Torneos", # Asegúrate de que esta app esté registrada si es donde tienes tus modelos/vistas
    "torneosArgentina", # Esta es tu app principal o la que contiene settings.py
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


STATIC_URL = '/static/'

# Directorios donde Django buscará tus archivos estáticos (CSS, JS, imágenes)
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "Torneos", "static"), # <-- ¡Esta es la ruta que debería funcionar!
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
