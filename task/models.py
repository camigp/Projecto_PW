from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    detecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class StudentModel(models.Model):
    nombre = models.CharField(max_length=50)

class TemaTesisModel(models.Model):
    nombre : models.CharField(max_length=100)
    descripcion: models.TextField(max_length=100)
    fuente: models.CharField(max_length=50)

class PerfilModel(models.Model):
    objeto_estudio = models.CharField(blank=True , max_length= 100)
    campo_accion = models.CharField(blank=True , max_length= 100)
    contexto_problema = models.TextField()
    aprobado = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profesor(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='nombres')
    apellidos = models.CharField(max_length=50, verbose_name='apellidos')
    ci = models.PositiveIntegerField(verbose_name='Carnet Identidad')
    nivel_escolar = models.CharField(verbose_name='Categoria Docente', max_length=10, choices=(
        ('1', 'Profesor'),
        ('2', 'Decano'),
        ('3', 'Vicidecano')
    ), default='1')

    # def __str__(self):
    #     return self.title + '- by ' + self.user.username
