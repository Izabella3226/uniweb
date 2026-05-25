from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from estudiantes.views import home, saludo
from django.contrib import admin
from django.urls import path
from estudiantes.views import guardar_estudiante, lista_estudiantes
from estudiantes.views import (
    saludo, 
    home, 
    registrar_producto,
    lista_productos,
    editar_producto,
    eliminar_producto
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("saludo/", saludo),
    path("productos/registro/", registrar_producto, name="registrar_producto"),
    path("productos/", lista_productos, name="lista_productos"),
    path("productos/editar/<int:id>/", editar_producto, name="editar_producto"),
    path("productos/eliminar/<int:id>/", eliminar_producto, name="eliminar_producto"),
    path("estudiantes/registro/", guardar_estudiante, name="guardar_estudiante"),
    path("estudiantes/", lista_estudiantes, name ="lista_estudiantes"),
    ]