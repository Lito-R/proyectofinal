from django.db import models

# Create your models here.
class Tarea(models.Model):
    tarea = models.CharField(max_length=100)

    def __str__(self):
        return self.tarea

class Actividad(models.Model):
    actividad = models.CharField(max_length=100)
    
    def __str__(self):
        return self.actividad
    