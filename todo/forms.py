from django import forms
from .models import Tarea, Actividad

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['tarea'] 

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['actividad'] 