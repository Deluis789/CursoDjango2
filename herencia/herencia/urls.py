from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('herencia/', views.herencia, name='herencia'),
    path('otra/', views.otra, name='otra'),
    path('ejemplo/', views.ejemplo, name='ejemplo'),
    path('', views.index, name='index')
]
