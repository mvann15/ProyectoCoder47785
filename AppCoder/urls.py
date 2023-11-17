
from django.contrib import admin
from django.urls import path
from AppCoder.views import crear_curso, show_html, mostrar_cursos
urlpatterns = [
    path('show/', show_html),
    path('agregar_curso/', crear_curso),
    path('cursos/', mostrar_cursos),

]
