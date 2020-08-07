from django.contrib import admin
from Modelado import models

# Register your models here.

admin.site.register(models.Usuario)
admin.site.register(models.Proyecto)
admin.site.register(models.Administrador)
admin.site.register(models.UnirseProyecto)
admin.site.register(models.Materias)
admin.site.register(models.EnviarSolicitud)
admin.site.register(models.Actividad)
admin.site.register(models.Events)

