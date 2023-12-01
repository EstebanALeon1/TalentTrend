from django import forms
from . models import Oferta

class FormularioOferta(forms.ModelForm):
    class Meta:
        model=Oferta
        fields='__all__'