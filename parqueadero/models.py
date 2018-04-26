from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse


# Create your models here.
class Propietario(models.Model):
    """ Categorias para clasificar las fotos """
    
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('propietario-list')


class Vehiculo(models.Model):
    """ Fotos del album """

    propietario = models.ForeignKey(Propietario, on_delete=models.PROTECT )
    codigo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50 )
    placa = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.codigo

    def get_absolute_url(self):
        return reverse('vehiculo-list')