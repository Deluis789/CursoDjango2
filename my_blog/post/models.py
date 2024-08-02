from datetime import date
from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre
    
class Entrar(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    headline = models.CharField(max_length=150)
    body_text = models.TextField()
    public_date = models.DateField(default=date.today)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
