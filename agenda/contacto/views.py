from django.shortcuts import render
from .models import Contacto

# Create your views here.
def index(request):
    contactos = Contacto.objects.filter(nombre__contains=request.GET.get('search', ''))
    context = {
        'contacto': contactos
    }
    return render(request, 'contacto/index.html', context)