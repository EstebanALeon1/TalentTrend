from django import forms
from . models import Experiencia

class FormularioExperiencia(forms.ModelForm):
    class Meta:
        model=Experiencia
        fields='__all__'