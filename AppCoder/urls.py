
from django.contrib import admin
from django.urls import path
from AppCoder.views import crear_curso, show_html
urlpatterns = [
    path('show/', show_html),
    path('agregar_curso/', crear_curso),

]
