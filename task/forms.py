from django.forms import ModelForm

from .models import TaskModel, PerfilTesisModel


class TaskForm(ModelForm):
    class Meta:
        model = TaskModel
        fields = ("title", "description", "important")


class PerfilForm(ModelForm):
    class Meta:
        model = PerfilTesisModel
        fields = ("tema","objeto_estudio", "campo_accion", "contexto_problema", "aprobado")


