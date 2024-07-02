from django import forms
from .models import Perfildev,Producto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }
class Perfil_dev_form(forms.ModelForm):
        class Meta:
             model = Perfildev
             fields = ['nombre_perfil','imagen_perfil','sobremi','github_perfil','correo_perfil']

class Productos_form(forms.ModelForm):
        class Meta:
             model = Producto
             fields = ['titulo_proyecto','archivo_proyecto','categoria_proyecto','descripcion_proyecto']
           