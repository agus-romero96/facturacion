import os
import django
from django.conf import settings

# Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_bd.settings')
django.setup()

from facturacion.models import Cliente,Producto

def ObtenerClientes():
    return [f"{cliente.cedula} - {cliente.nombre} {cliente.apellido}" for cliente in Cliente.objects.all()]
