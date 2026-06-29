import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config_mercado.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username='Admin').exists():
    User.objects.create_superuser('Admin', 'digitalpro2999@gmail.com', 'Ger$0n')
    print("Superusuario creado con éxito.")
else:
    print("El superusuario ya existe.")
