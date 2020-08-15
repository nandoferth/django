from django.db import models

# Create your models here.
class productos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=100)