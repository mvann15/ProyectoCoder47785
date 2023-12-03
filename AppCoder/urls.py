from django.contrib import admin
from django.urls import path
from AppCoder.views import CursoList, \
    CursoDetalle, CursoCreacion, CursoActualizacion, CursoEliminar

urlpatterns = [
    path('cursos/listar/', CursoList.as_view(), name="CursosList"),
    path('curso/<int:pk>', CursoDetalle.as_view(), name="CursoDetail"),
    path('crear', CursoCreacion.as_view(), name="CursoCreate"),
    path('editar/<int:pk>', CursoActualizacion.as_view(), name="CursoEditar"),
    path('eliminar/<int:pk>', CursoEliminar.as_view(), name="CursoEliminar"),
]
