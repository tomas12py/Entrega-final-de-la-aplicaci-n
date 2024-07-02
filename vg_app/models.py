from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Desarrolladores(models.Model):
    iddev = models.AutoField(primary_key = True)
    correodev_1 = models.CharField(max_length = 100)
    telefonodev = models.IntegerField

class Clientes(models.Model):
    idcliente = models.AutoField(primary_key = True)
    nususario = models.CharField(max_length = 50)
    correou = models.CharField(max_length = 100)
    contraseña  = models.CharField(max_length = 50) 
    pagos = models.FloatField   

class Perfildev(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    imagen_perfil  = models.ImageField(upload_to = 'imagenes/',blank = True)
    nombre_perfil  = models.CharField(max_length = 50,blank = True)
    correo_perfil  = models.EmailField(max_length = 100,blank = True)
    github_perfil  = models.URLField(max_length = 100,blank = True)
    youtube_perfil  = models.CharField(max_length = 100,blank = True)
    twitch_perfil  = models.CharField(max_length = 100,blank = True)
    facebook_perfil  = models.CharField(max_length = 100,blank = True)
    instagram_perfil  = models.CharField(max_length = 100,blank = True)
    sobremi  = models.TextField(blank = True)
class Comunidad(models.Model):
    id_comunidad = models.AutoField(primary_key = True)
    archivo_publicacion = models.FileField
    likes_publicacion = models.IntegerField
    comentarios_publicacion = models.TextField

class Finanzas(models.Model):
    idfinanzas = models.AutoField(primary_key = True)
    ganancia_dev = models.FloatField
    ganancia_pagina = models.FloatField

class Producto(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    titulo_proyecto = models.CharField(max_length = 100,blank = True)
    descripcion_proyecto = models.TextField(blank = True)
    categoria_proyecto =  models.CharField(max_length = 50,blank = True)
    archivo_proyecto = models.FileField(blank = True)