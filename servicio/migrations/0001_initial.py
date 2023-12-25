# Generated by Django 5.0 on 2023-12-25 06:19

import cloudinary.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_convenio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=1000)),
                ('imagen', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=1000)),
                ('enlace', models.CharField(max_length=200)),
                ('imagen', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('num_telefono', models.CharField(max_length=25)),
                ('tipo_convenio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicio.categoria_convenio')),
            ],
        ),
        migrations.CreateModel(
            name='Especialista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=15)),
                ('num_telefono', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=1000)),
                ('horarios', models.CharField(max_length=150)),
                ('administrador', models.BooleanField(default=False)),
                ('imagen', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('convenio', models.ManyToManyField(related_name='especialista_convenio', to='servicio.convenio')),
                ('especialidad', models.ManyToManyField(related_name='especialista_especialidad', to='servicio.especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('num_telefono', models.CharField(max_length=25)),
                ('motivo_consulta', models.CharField(max_length=500)),
                ('especialista_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='servicio.especialista')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=1000)),
                ('imagen', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('especialidades', models.ManyToManyField(related_name='servicios', to='servicio.especialidad')),
            ],
        ),
    ]
