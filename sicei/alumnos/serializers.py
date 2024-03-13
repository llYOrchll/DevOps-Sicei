from rest_framework import serializers
from .models import listaAlumnos

class alumnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = listaAlumnos
        fields = ['__all__']
