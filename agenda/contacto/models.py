from django.db import models
from datetime import date

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    telefono = models.CharField(max_length=12, blank=True, null=True)
    celular = models.CharField(max_length=12, blank=False, null=False)
    email = models.EmailField()
    compania = models.CharField(max_length=20, blank=True, null=True)
    fecha  = models.DateField(default=date.today)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre