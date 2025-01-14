from django.db import models
from datetime import date

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    short_description = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=False, null=False)
    stock = models.IntegerField(default=20)
    disconunt_until = models.DateField(default=date.today)

    def __str__(self):
        return self.name