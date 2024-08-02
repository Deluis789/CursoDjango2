from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=150, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=300, null=True)
    date = models.DateField(null= True) 
    siganture = models.CharField(max_length=100, default='Firma')

    def __str__(self):
        return self.name


