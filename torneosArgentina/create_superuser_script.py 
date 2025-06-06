import os
import django
import sys # Importa sys para un manejo de salida más limpio

# Configura el entorno de Django
# Asegúrate de que 'torneosArgentina' es el nombre de tu proyecto principal (la carpeta que contiene settings.py)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'torneosArgentina.settings')
django.setup()

from django.contrib.auth import get_user_model

# Obtiene el modelo de usuario (User)
User = get_user_model()

# Define las credenciales del superusuario (pueden ser sobrescritas por variables de entorno de Render)
username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'temporal123') # <-- ¡CRÍTICO: CAMBIA ESTA CONTRASEÑA POR UNA SEGURA DESPUÉS DE INICIAR SESIÓN!

# Crea el superusuario solo si no existe
if not User.objects.filter(username=username).exists():
    # Usamos sys.stdout.write y flush para asegurar que la salida se muestre en los logs de Render
    sys.stdout.write(f"Creando superusuario {username}...\n")
    sys.stdout.flush()
    try:
        User.objects.create_superuser(username, email, password)
        sys.stdout.write(f"Superusuario {username} creado exitosamente.\n")
        sys.stdout.flush()
    except Exception as e:
        sys.stderr.write(f"Error al crear superusuario {username}: {e}\n")
        sys.stderr.flush()
        sys.exit(1) # Salir con un código de error si falla la creación
else:
    sys.stdout.write(f"Superusuario {username} ya existe.\n")
    sys.stdout.flush()
    # Si quieres restablecer la contraseña en cada despliegue, descomenta esto:
    # try:
    #     user = User.objects.get(username=username)
    #     user.set_password(password)
    #     user.save()
    #     sys.stdout.write(f"Contraseña de superusuario {username} restablecida.\n")
    #     sys.stdout.flush()
    # except Exception as e:
    #     sys.stderr.write(f"Error al restablecer contraseña para {username}: {e}\n")
    #     sys.stderr.flush()
    #     sys.exit(1)
