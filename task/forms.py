from django.forms import ModelForm

from .models import PerfilTesisModel



class PerfilForm(ModelForm):
    class Meta:
        model = PerfilTesisModel
        fields = ("tema","objeto_estudio", "campo_accion", "contexto_problema", "aprobado")


