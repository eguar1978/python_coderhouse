from django import forms
from .models import Celular, Computadora, Televisor

class CelularForm(forms.ModelForm):
    class Meta:
        model = Celular
        fields = '__all__'

class ComputadoraForm(forms.ModelForm):
    class Meta:
        model = Computadora
        fields = '__all__'

class TelevisorForm(forms.ModelForm):
    class Meta:
        model = Televisor
        fields = '__all__'
