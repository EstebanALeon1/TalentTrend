from django.db import models

# Create your models here.
class Oferta(models.Model):
    nombre=models.CharField(max_length=50)
    tipo_contrato=models.CharField(max_length=25)
    cargo=models.CharField(max_length=25)
    cuoc=models.IntegerField()    
    salario=models.IntegerField()
    tipo_empleo=models.CharField(max_length=25)
    n_vacantes=models.IntegerField()
    n_postulaciones=models.IntegerField()


    def __str__(self):
        return self.nombre