from django.db import models
from cloudinary.models import CloudinaryField

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    valor = models.IntegerField()
    necesita_receta = models.BooleanField(default=False)
    imagen = CloudinaryField('image')
    categoria = models.ManyToManyField('Categoria',related_name='productos_categoria')

    def __str__(self):
        return self.nombre
