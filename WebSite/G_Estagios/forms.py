from django import forms
from .models import Curso,Polo

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome_curso', 'Polo']
