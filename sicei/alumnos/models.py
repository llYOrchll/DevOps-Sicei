from django.db import models

# Create your models here.
class alumnos_lista:
    def __init__(self, id, nombre, matricula):
        self.id = id
        self.nombre = nombre
        self.matricula = matricula

    def __str__(self):
        return f"ID: {self.id}\nNombre: {self.nombre}\nMatricula: {self.matricula}"
    
alumno1 = alumnos_lista("1", "Jorge", "A15003810")
alumno1 = alumnos_lista("2", "Pablo", "A18009859")