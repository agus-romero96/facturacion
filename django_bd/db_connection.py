import os
import django
from django.conf import settings

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_bd.settings')
django.setup()

from facturacion.models import Cliente

def ObtenerClientes():
    return [str(cliente) for cliente in Cliente.objects.all()]  # Devuelve una lista de clientes