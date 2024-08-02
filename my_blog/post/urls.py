from django.urls import path
from . import views

urlpatterns = [
    path('querys/', views.querys, name='querys'),
    path('update/', views.update, name='update'),
    
]