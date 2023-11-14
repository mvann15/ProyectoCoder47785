from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso


def crear_curso(request):
    curso = Curso(nombre="Python", camada=47785)
    curso.save()

    return HttpResponse(f"Su curso es {curso.nombre} y su camada es {curso.camada}")
