"""
URL configuration for vg_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from vg_app.views import inicio,perfil,categorias,pago,comunidad,Logup,Proyectos,eliminar,editar_producto,edicion_completada
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('',inicio,name = 'inicio'),
    path('perfil',perfil),
    path('categorias',categorias),
    path('pago',pago),
    path('comunidad',comunidad),
    path('logup',Logup),
    path('proyectos',Proyectos),
    path('login', LoginView.as_view(template_name='login.html')),
    path('logout', LogoutView.as_view(template_name='inicio.html'),name = 'logout'),
    path('eliminar/<id>',eliminar),
    path("editar/<id>",editar_producto),
    path("edicion-completada/",edicion_completada)
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

