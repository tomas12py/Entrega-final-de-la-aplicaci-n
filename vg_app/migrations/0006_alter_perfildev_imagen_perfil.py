# Generated by Django 5.0.4 on 2024-06-30 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vg_app', '0005_alter_perfildev_imagen_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfildev',
            name='imagen_perfil',
            field=models.ImageField(blank=True, default='imagenes/icono.jpg', upload_to='imagenes/'),
        ),
    ]
