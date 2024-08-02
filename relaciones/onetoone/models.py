from django.db import models

# Create your models here.
class Lugar(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre  
    
class Restaurante(models.Model):
    lugar = models.OneToOneField(Lugar, on_delete=models.CASCADE, primary_key=True)
    numero_de_empleados = models.IntegerField(default=1)

    def __str__(self):
        return self.lugar.nombre

