from django.db import models

# Create your models here.
class Reloj (models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=20)
    tipo = models.CharField(max_length=5)
    material = models.CharField(max_length=30)
    precio = models.FloatField()
    ano_lanzamiento = models.DateField()
    
    def __str__(self):
        return self.marca     