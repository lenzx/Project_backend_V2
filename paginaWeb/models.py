from django.db import models

# Create your models here.
from cloudinary.models import CloudinaryField

class Markay(models.Model):
    imagen = CloudinaryField('image')
    descripcion = models.CharField(max_length=1000)

class Seccion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    
class Red_social(models.Model):
    imagen = CloudinaryField('image')
    enlace = models.CharField(max_length=200)
    texto = models.CharField(max_length=100)