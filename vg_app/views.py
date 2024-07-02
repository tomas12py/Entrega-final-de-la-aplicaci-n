from django.shortcuts import render,redirect
from .models import *
from .forms import UserRegisterForm,Perfil_dev_form,Productos_form
from django.contrib.auth.decorators import login_required
# Create your views here.
def inicio(request):
    return render (request,"inicio.html")
@login_required
def perfil(request):
    perfil_datos = Perfildev.objects.filter(user = request.user)

    proyectos_datos = Producto.objects.all().filter(user = request.user)
    if request.method == 'POST':
        form = Perfil_dev_form(request.POST,request.FILES)
        if form.is_valid():
            form.user = request.user 
            nombre_perfil = form.cleaned_data.get('nombre_perfil')
            imagen_perfil = form.cleaned_data.get('imagen_perfil')
            sobremi =  form.cleaned_data.get('sobremi')
            github_perfil =  form.cleaned_data.get('github_perfil')
            correo_perfil =  form.cleaned_data.get('correo_perfil')
            p,create = Perfildev.objects.get_or_create(user=form.user,nombre_perfil=nombre_perfil,imagen_perfil = imagen_perfil,sobremi = sobremi,github_perfil = github_perfil,correo_perfil = correo_perfil)
            p.save()
    else:
        form = Perfil_dev_form()
    context = {'perfil_datos':perfil_datos,'form':form,'proyecto_datos':proyectos_datos}
    return render(request,'perfil.html',context)
@login_required
def pago(request):
    return render(request,"pago.html")
@login_required
def categorias(request):        
    return render(request,"categorias.html")
@login_required
def comunidad(request):
    return render(request,"comunidad.html")
def Logup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegisterForm()  
    return render(request,"logup.html",{'form':form})

@login_required
def Proyectos(request):
    if request.method == 'POST':
        form = Productos_form(request.POST,request.FILES)
        if form.is_valid():
            form.user = request.user
            titulo_proyecto = form.cleaned_data.get('titulo_proyecto')
            descripcion_proyecto = form.cleaned_data.get('descripcion_proyecto')
            archivo_proyecto = form.cleaned_data.get('archivo_proyecto')
            categoria_proyecto = form.cleaned_data.get('categoria_proyecto')
            productos,created = Producto.objects.get_or_create(user = form.user,titulo_proyecto = titulo_proyecto,descripcion_proyecto = descripcion_proyecto,archivo_proyecto = archivo_proyecto,categoria_proyecto = categoria_proyecto)
            productos.save()
            return redirect("/perfil")
    return render(request,"proyectos.html")
@login_required
def eliminar(request,id):
    curso = Producto.objects.get(id=id)
    curso.delete()
    return redirect("/perfil")
@login_required
def editar_producto(request,id):
    producto = Producto.objects.get(id=id)
    return render(request, "edicion.html", {"edicion_producto": producto})
@login_required
def edicion_completada(request):
    titulo_proyecto = request.POST["titulo_proyecto"]
    descripcion_proyecto = request.POST["descripcion_proyecto"]
    categoria_proyecto = request.POST["categoria_proyecto"]
    archivo_proyecto = request.FILES["archivo_proyecto"]
    id = request.POST["id"]
    producto = Producto.objects.get(id = id)
    producto.titulo_proyecto = titulo_proyecto
    producto.descripcion_proyecto = descripcion_proyecto
    producto.categoria_proyecto = categoria_proyecto
    producto.archivo_proyecto = archivo_proyecto
    producto.save()

    return redirect("/perfil")