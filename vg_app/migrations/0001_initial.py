# Generated by Django 5.0.4 on 2024-06-28 00:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('idcliente', models.AutoField(primary_key=True, serialize=False)),
                ('nususario', models.CharField(max_length=50)),
                ('correou', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comunidad',
            fields=[
                ('id_comunidad', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Desarrolladores',
            fields=[
                ('iddev', models.AutoField(primary_key=True, serialize=False)),
                ('correodev_1', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Finanzas',
            fields=[
                ('idfinanzas', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_proyecto', models.CharField(blank=True, max_length=100)),
                ('descripcion_proyecto', models.TextField(blank=True)),
                ('categoria_proyecto', models.CharField(blank=True, max_length=50)),
                ('archivo_proyecto', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Perfildev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen_perfil', models.ImageField(blank=True, upload_to='imagenes/')),
                ('nombre_perfil', models.CharField(blank=True, max_length=50)),
                ('correo_perfil', models.EmailField(blank=True, max_length=100)),
                ('github_perfil', models.URLField(blank=True, max_length=100)),
                ('youtube_perfil', models.CharField(blank=True, max_length=100)),
                ('twitch_perfil', models.CharField(blank=True, max_length=100)),
                ('facebook_perfil', models.CharField(blank=True, max_length=100)),
                ('instagram_perfil', models.CharField(blank=True, max_length=100)),
                ('sobremi', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
