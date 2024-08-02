from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.
def test(request): 
    return HttpResponse('Hola mundo funciona')

def create(request):
    #comment = Comment(name="juanjo", score="5", comment= "Este es un comentario")
    #comment.save()
    comment = Comment.objects.create(name="Alex")
    return HttpResponse('Crearrrrr...')

def delete(request):
    #comment = Comment.objects.get(id=4)
    #comment.delete()
    Comment.objects.filter(id=2).delete()
    return HttpResponse('Se ha eliminado')