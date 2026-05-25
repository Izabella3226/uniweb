from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Estudiante
from.models import Producto

def saludo(request):
    return HttpResponse("Hola desde el servidor (django)")

def home(request):
    contexto={"titulo":"Home Estudiantes"}
    return render(request, "estudiantes/home.html", contexto)

def guardar_estudiante(request):
    if request.method == "POST":
      nombre = request.POST.get("nombre")
      edad = int(request.POST.get("edad"))
    
      Estudiante.objects.create(nombre=nombre, edad=edad)
      return redirect("lista_estudiantes")
    return render(request, "estudiantes/registro_estudiante.html")
    
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request,"estudiantes/lista_productos.html", {"productos": productos})  
 
def registrar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")

        Producto.objects.create(
        nombre = nombre,
        precio=precio
        )
        return redirect("lista_productos")

    return render(request, "estudiantes/registro_producto.html")

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)

    if request.method == "POST":
        producto.nombre = request.POST.get("nombre")
        producto.precio = request.POST.get("precio")
        producto.save()

        return redirect("lista_productos")

    return render(request, "estudiantes/editar_producto.html", {
        "producto": producto
    })
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()

    return redirect("lista_productos")
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "estudiantes/lista_estudiantes.html",{
        "estudiantes": estudiantes
    })
