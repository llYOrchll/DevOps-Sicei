from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import listaAlumnos
from .serializers import alumnosSerializer

class alumnoView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            alumno = listaAlumnos.get(pk=pk)
            serializer = alumnosSerializer(alumno)
            return Response(serializer.data)
        else:
            alumnos = listaAlumnos.objects.all()
            serializer = alumnosSerializer(alumnos, many=True)
            return Response(serializer.data)
        
    def post(self, request):
        serializer = alumnosSerializer(data=request.data)
        if serializer.is_valis():
            serializer.save()
            return Response(serializer.data, status=status._CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        if pk is not None:
            alumno = listaAlumnos.objects.get(pk=pk)
            serializer = alumnosSerializer(alumno, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Provide a valid student ID'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is not None:
            alumno = listaAlumnos.objects.get(pk=pk)
            alumno.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            alumnos = listaAlumnos.objects.all()
            alumnos.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


"""def crear_alumno(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        matricula = request.POST.get('matricula')
        alumno = alumnos_lista.objects.create(id=id, nombre=nombre, matricula=matricula)
        return JsonResponse({'id': alumno.id, 'nombre': alumno.nombre, 'matricula': alumno.matricula})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def editar_alumno(request, id):
    try:
        alumno = alumnos_lista.objects.get(id=id)
    except alumnos_lista.DoesNotExist:
        return JsonResponse({'error': 'Alumno no encontrado'}, status=404)
    
    if request.method == 'PUT':
        nombre = request.PUT.get('nombre')
        matricula = request.PUT.get('matricula')
        alumno.nombre = nombre
        alumno.matricula = matricula
        alumno.save()
        return JsonResponse({'message': 'Alumno actualizado correctamente'})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

def eliminar_alumno(request, id):
    try:
        alumno = alumnos_lista.objects.get(id=id)
    except alumnos_lista.DoesNotExist:
        return JsonResponse({'error': 'Alumno no encontrado'}, status=404)
    if request.method == 'DELETE':
        alumno.delete()
        return JsonResponse({'message': 'Alumno eliminado correctamente'})"""