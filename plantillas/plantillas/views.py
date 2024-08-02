from django.http import HttpResponse
from django.shortcuts import render

def simple(request):
    return render(request, 'simple.html')

def dinamico(request, name):
    categories = ['Frutas', 'Verduras', 'Ortalizas']
    context = {
        'name': name,
        'categories': categories
    }
    return render(request, 'plantilla.html', context)