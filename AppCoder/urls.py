
from django.contrib import admin
from django.urls import path
from AppCoder.views import crear_curso, show_html, mostrar_cursos, crear_curso_form, busqueda_camada
urlpatterns = [
    path('show/', show_html),
    path('agregar_curso/', crear_curso),
    path('buscar/', busqueda_camada),
    path('curso/', crear_curso_form),
    path('cursos/', mostrar_cursos),

]
