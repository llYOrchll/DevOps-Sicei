from django.db import models
# Create your models here.
class listaAlumnos(models.Model):
    nombre = models.CharField(max_length=15)
    matricula = models.CharField(max_length=9)