from django.db import models
from django.forms import ModelForm
# Create your models here.

class Usuario(models.Model):
    sex=(
        ('M','M'),
        ('F','F'),
    )
    name = models.CharField(max_length=30, null=True)
    apellido = models.CharField(max_length=30, null=True)
    nickname = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=254,null=True)
    sexo = models.CharField(max_length = 10, null=True, choices=sex,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name

class Materias(models.Model):
    name = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name

class Proyecto(models.Model):
    
    name = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
    usuario = models.ManyToManyField(Usuario)
    materia = models.ManyToManyField(Materias,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Administadores(models.Model):
    usuario = models.ManyToManyField(Usuario)
    proyecto = models.ForeignKey(Proyecto,null=True,on_delete=models.SET_NULL)

class Administrador(models.Model):
    usuario = models.ForeignKey(Usuario,null=True,on_delete=models.SET_NULL)
    proyecto = models.ForeignKey(Proyecto,null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return 'Proyecto: %s Administrador: %s'%(self.proyecto.name,self.usuario.name)

class UnirseProyecto(models.Model):
    estatus=(
        ('Espera','Espera'),
        ('Confirmar','Confirmar'),
        ('Eleminar','Eleminar'),
    )
    usuario = models.ForeignKey(Usuario,null=True,on_delete=models.SET_NULL)
    proyecto = models.ForeignKey(Proyecto,null=True,on_delete=models.SET_NULL)
    estatu = models.CharField(max_length=10,null=True,choices=estatus)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def  __str__(self):
        return self.usuario.name

class SolicitudProyecto(models.Model):
    estatus=(
        ('Espera','Espera'),
        ('Confirmar','Confirmar'),
        ('Eleminar','Eleminar'),
    )
    proyecto = models.ForeignKey(Proyecto,null=True,on_delete=models.SET_NULL)
    usuario = models.ManyToManyField(Usuario)
    estatu = models.CharField(max_length=10,null=True,choices=estatus)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def  __str__(self):
        return self.proyecto

class EnviarSolicitud(models.Model):
    usuario = models.OneToOneField(Usuario,on_delete=models.CASCADE)
    agregar_usuario = models.ManyToManyField(Usuario,related_name='is_following', blank=True)
    follwers = models.ManyToManyField(Usuario,related_name='is_followers', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.usuario.name


class Actividad(models.Model):
    importancia=(
        ('important','important'),
        ('info','info'),
    )
    name = models.CharField(max_length=100, null=True)
    inicio_año = models.IntegerField(blank=True, null=True)
    inicio_mes = models.IntegerField(blank=True, null=True)
    inicio_dia = models.IntegerField(blank=True, null=True)
    inicio_hora = models.IntegerField(blank=True, null=True)
    inicio_min = models.IntegerField(blank=True, null=True)
    escoge_importancia = models.CharField(max_length=10,null=True,choices=importancia)
    proyecto = models.ManyToManyField(Proyecto)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Events(models.Model):
    importancia=(
        ('important','important'),
        ('info','info'),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    escoge_importancia = models.CharField(max_length=10,null=True,choices=importancia)
    proyecto = models.ManyToManyField(Proyecto)
    usuario = models.ManyToManyField(Usuario, blank=True)
    event_type = models.CharField(max_length=10,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
#f
