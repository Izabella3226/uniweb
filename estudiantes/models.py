from django.db import models # type: ignore

class Estudiante(models.Model):
    nombre=models.CharField(max_length=100)
    edad=models.IntegerField()

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def _str_(self):
        return self.nombre

# Create your models here.