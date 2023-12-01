from django.db import models

# Create your models here.
class Experiencia(models.Model):
    empresa=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=250)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()    
    cargo=models.CharField(max_length=50)
    funciones=models.CharField(max_length=250)
    


    def __str__(self):
        return self.empresa