from django.http import JsonResponse
from .models import alumnos_lista

def lista_alumnos(request):
    alumnos = alumnos_lista.objects.all()
    data = [{'id': alumnos.id, 'nombre': alumnos.nombre, 'matricula': alumnos.matricula} for alumnos in alumnos_lista]
    return JsonResponse(data, safe=False)

def obtener_alumno(request, id):
    try:
        alumno = alumnos_lista.objects.get(id=id)
    except alumnos_lista.DoesNotExist:
        return JsonResponse({'error': 'Alumno no encontrado'}, status=404)
    if request.method == 'GET':
        id = request.get('id')
        nombre = request.get('nombre')
        matricula = request.get('matricula')
        return JsonResponse({'ID: ':id, '\nNombre: ':nombre, '\Matricula: ':matricula})


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