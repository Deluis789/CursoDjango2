from django.db import models
from datetime import date 

# Create your models here.
class Todo(models.Model):
    titulo = models.CharField(max_length=70, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField(default=date.today)
    fin_fecha = models.DateField(blank=True, null=True)
    prioridad = models.IntegerField(default=3)

    def __str__(self):
        return self.titulo