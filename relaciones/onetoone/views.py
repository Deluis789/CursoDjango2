from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugar, Restaurante

# Create your views here.
def crear(request):
    # Creamos elementos en esta parte 
    lugar = Lugar(nombre = 'Lugar 1', direccion = 'Calle Avaroa')
    lugar.save()
    restaurante = Restaurante(lugar = lugar, numero_de_empleados = 8)
    restaurante.save()

    return HttpResponse(restaurante.lugar.nombre)
