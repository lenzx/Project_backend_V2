from django.db import models
from cloudinary.models import CloudinaryField

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)
    valor = models.IntegerField()
    necesita_receta = models.BooleanField(default=False)
    imagen = CloudinaryField('image')
    categoria = models.ManyToManyField(Categoria,through='Producto_categoria',related_name='productos')

class Producto_categoria(models.Model):
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)



