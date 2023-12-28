from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.utils import timezone



class Especialista(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=15)
    num_telefono = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=1000)
    horarios = models.CharField(max_length=150)
    administrador = models.BooleanField(default=False)
    imagen = CloudinaryField('image')
    convenio = models.ManyToManyField('Convenio', related_name='especialista_convenio', blank=True)
    especialidad = models.ManyToManyField('Especialidad', related_name='especialista_especialidad', blank=True)

    def __str__(self):
        return self.nombre


class Convenio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    enlace = models.CharField(max_length=200)
    direccion = models.CharField(max_length=100, default="")
    imagen = CloudinaryField('image', folder='convenios_img')
    num_telefono = models.CharField(max_length=25)
    tipo_convenio_id = models.ForeignKey('Categoria_convenio', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.nombre


class Categoria_convenio(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Especialidad(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    imagen = CloudinaryField('image')
    servicios = models.ManyToManyField('Servicio', related_name='especialidades_servicios', blank=True)
    

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    imagen = CloudinaryField('image')

    def __str__(self):
        return self.nombre
class Consulta(models.Model):
    nombre = models.CharField(max_length=200)
    correo_electronico = models.EmailField()
    num_telefono = models.CharField(max_length=25)
    motivo_consulta = models.CharField(max_length=500)
    especialista_id = models.ForeignKey('Especialista', on_delete=models.CASCADE, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre

