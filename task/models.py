from django.contrib.auth.models import User
from django.db import models
from django.forms import BooleanField


class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length= 50)
    correo = models.EmailField()
    contrasenna = models.CharField(max_length=50)
    nombre = models.CharField(max_length= 50)
    apellidos = models.CharField(max_length=50)

class StudentModel(models.Model):
    user = Usuario(Usuario, on_delete=models.CASCADE)
    merito_cientifico = BooleanField(default = False)

class PerfilTesisModel(models.Model):
    tema = models.ForeignKey(TemaTesisModel , on_delete=models.CASCADE)
    objeto_estudio = models.CharField(blank=True , max_length= 100)
    campo_accion = models.CharField(blank=True , max_length= 100)
    contexto_problema = models.TextField()
    aprobado = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class TemaTesisModel(models.Model):
    nombre : models.CharField(max_length=100)
    descripcion: models.TextField(max_length=100)
    fuente: models.CharField(max_length=50)
    # cant_perfiles = models.CharField(max_length=50)



class Profesor(models.Model):

    nivel_escolar = models.CharField(verbose_name='Categoria Docente', max_length=10, choices=(
        ('1', 'Profesor'),
        ('2', 'Decano'),
        ('3', 'Vicidecano')
    ), default='1')




    # def __str__(self):
    #     return self.title + '- by ' + self.user.username
