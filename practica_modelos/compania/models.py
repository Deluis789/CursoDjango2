from django.db import models

# Create your models here.

class Salario(models.Model):
    cantidad = models.IntegerField(null=False, blank=False)
    extra_dic = models.BooleanField(default=False)
    extra_jun = models.BooleanField(default=False)

    def __str__(self):
        return self.cantidad
    
class Cargo(models.Model):
    titulo = models.CharField(max_length=15, blank=False, null=False)
    descripcion = models.TextField(null=False)
    salario = models.ForeignKey(Salario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Pais(models.Model):
    nombre = models.CharField(max_length=15, blank=False, null=False)
    codigo_ciudad = models.CharField(max_length=6, blank=False, null=False)

    def __str__(self):
        return self.nombre

class Localizacion(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)
    ciudad = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Lugar(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    codigo_postal = models.CharField(max_length=5, null=False, blank=False)
    localizacion = models.ForeignKey(Localizacion, on_delete=models.CASCADE)

    def __str__(self):
        self.nombre
    
class Empleado(models.Model):
    dni = models.CharField(max_length=8, blank=False, null=False)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False)
    direccion = models.CharField(max_length=50, blank=False, null=False)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre