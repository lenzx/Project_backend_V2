from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User



class Especialista(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=15)
    num_telefono = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=1000)
    horarios = models.CharField(max_length=150)
    administrador = models.BooleanField(default=False)
    imagen = CloudinaryField('image')


class Categoria_convenio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Convenio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    enlace = models.CharField(max_length=200)
    imagen = CloudinaryField('image', folder='convenios_img')
    num_telefono = models.CharField(max_length=25)
    tipo_convenio_id = models.ForeignKey(Categoria_convenio, on_delete=models.CASCADE)
    especialistas = models.ManyToManyField(Especialista,through='Especialista_convenio',related_name='convenios')


class Especialista_convenio(models.Model):
    especialista_id = models.ForeignKey(Especialista, on_delete=models.CASCADE)
    convenio_id = models.ForeignKey(Convenio, on_delete=models.CASCADE)
    
class Especialidad(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000)
    imagen = CloudinaryField('image')
    especialistas = models.ManyToManyField(Especialista,through='Especialista_especialidad',related_name='especialidades')

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    imagen = CloudinaryField('image')
    especialidades = models.ManyToManyField(Especialidad,through='Especialidad_servicio',related_name='servicios')

    def __str__(self):
        return self.nombre

class Especialidad_servicio(models.Model):
    servicio_id = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    especialidad_id = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    
class Especialista_especialidad(models.Model):
    especialista_id = models.ForeignKey(Especialista, on_delete=models.CASCADE)
    especialidad_id = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

class Consulta(models.Model):
    nombre = models.CharField(max_length=200)
    correo_electronico = models.EmailField()
    num_telefono = models.CharField(max_length=25)
    motivo_consulta = models.CharField(max_length=500)
    especialista_id = models.ForeignKey(Especialista, on_delete=models.CASCADE, null=True)

