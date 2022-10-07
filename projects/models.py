from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class project(models.Model):
    title=models.CharField(max_length=200,verbose_name='Titulo')
    descripcion=models.TextField(verbose_name='Descripcion')
    tecnology=models.CharField(max_length=200,verbose_name='Tipo')
    created_at=models.DateTimeField(verbose_name='Fecha de creacion',auto_now_add=True)