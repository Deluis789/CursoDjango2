from django.shortcuts import render
from django.http import HttpResponse
from .models import Autor,Entrar 

# Create your views here.
def querys(request):
    # Obtener todos los elementos
    autores = Autor.objects.all()

    # Obtener datos filtrados por condicion
    filtered = Autor.objects.filter(id=25)

    # Obtener un unico objeto (filtrado)
    filtroid = Autor.objects.get(id=1)

    #Obtener los 10 primeros elementos con limit []
    limit = Autor.objects.all()[:10]

    # Obtener 5 elementos saltando los cinco primeros
    offsets = Autor.objects.all()[5:10]

    # Obtener todos los elementos ordenados
    orders = Autor.objects.all().order_by('email')

    # Obtener todos los elementos cuyo id sea menor a igual a 15
    filtereds2 = Autor.objects.filter(id__lte=15)
    # Obtener todos los autores que contiene en su nombre la palabra yes
    filtereds3 = Autor.objects.filter(nombre__contains='yes')

    return render(request, 'post/querys.html', {'autores': autores, 
    'filtered':filtered, 'filtroid':filtroid, 'limit': limit, 'offsets':offsets, 'orders': orders, 'filtereds2': filtereds2,
    'filtereds3': filtereds3})

def update(request):
    autor = Autor.objects.get(id = 1)
    autor.nombre = 'Jorge'
    autor.email = 'diaz23@gmail.com'
    autor.save()

    return HttpResponse('Ya se actualizo los datos')