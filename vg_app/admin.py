from django.contrib import admin
from .models import Perfildev,Producto
# Register your models here.
class Admin_Perfildev(admin.ModelAdmin):
    fields = ["imagen_perfil","nombre_perfil","correo_perfil","github_perfil","youtube_perfil" ,"twitch_perfil","facebook_perfil" ,"instagram_perfil","sobremi","user"]
    list_display = ["nombre_perfil","sobremi","correo_perfil"]
admin.site.register(Perfildev,Admin_Perfildev)

admin.site.register(Producto)