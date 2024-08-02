from django.shortcuts import render
from django.http import HttpResponse

def getform(request):
    return render(request, 'form.html', {})

def getgoal(request):
    if request.method != 'GET':
        return HttpResponse('El metodo POST no esta soportado para esta ruta')
    
    nombre = request.GET['name'] 
    email = request.GET['email']
    return render(request, 'success.html', {'nombres': nombre, 'emails': email})

def postform(request):
    return render(request, 'postform.html', {})

def postgoal(request):
    if request.method != 'POST':
        return HttpResponse('El metodo GET no esta soportado para esta ruta') 

    nombre = request.POST['nombre']
    return render(request, 'postsuccess.html', {'nombres': nombre})