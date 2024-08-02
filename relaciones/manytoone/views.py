from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date
# Create your views here.
def crear(request):
    rep = Reporter(first_name='Luis', last_name='Ruiz', email= 'luisr@gmail.com')
    rep.save()

    art1 = Article(headline= 'es un headline', pub_date=date(2022,6,6), reporter= rep) 
    art1.save()
    art2 = Article(headline= 'lorem ipsum deate', pub_date=date(2022,1,6), reporter= rep)
    art2.save()
    art3 = Article(headline= 'Es unmmensaje random', pub_date=date(2022,9,4), reporter= rep) 
    art3.save()

    #result = art1.reporter.first_name
    result = rep.article_set.all()
    result = rep.article_set.filter(headline='lorem ipsum deate')
    result = rep.article_set.count()

    return HttpResponse(result)
