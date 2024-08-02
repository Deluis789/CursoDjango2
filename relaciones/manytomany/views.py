from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, Article
# Create your views here.
def crear(request):
    art1 = Article(headline= 'articulo_primero')
    art1.save()

    art2 = Article(headline= 'articulo_segundo')
    art2.save()

    art3 = Article(headline= 'articulo_tercero')
    art3.save()

    pub1 = Publication(title='publicacion_primera')
    pub1.save()
    pub2 = Publication(title='publicacion_segunda')
    pub2.save()
    pub3 = Publication(title='publicacion_tercera')
    pub3.save()
    pub4 = Publication(title='publicacion_cuarta')
    pub4.save()
    pub5 = Publication(title='publicacion_quinta')
    pub5.save()
    pub6 = Publication(title='publicacion_sexta')
    pub6.save()
    pub7 = Publication(title='publicacion_septima')
    pub7.save()

    art1.publications.add(pub1, pub2, pub3)
    art2.publications.add(pub4, pub5)
    art3.publications.add(pub6, pub7)

    result = art1.publications.all()
    pub1 = Publication.objects.get(id=1)
    result = pub1.article_set.all()


    return HttpResponse(result)