# Generated by Django 5.0.4 on 2024-06-30 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vg_app', '0007_alter_perfildev_imagen_perfil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfildev',
            name='imagen_perfil',
            field=models.ImageField(blank=True, upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='perfildev',
            name='nombre_perfil',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]