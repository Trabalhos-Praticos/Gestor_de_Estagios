from django import forms
from .models import Curso,Documento

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome_curso', 'Polo']

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['tipo', 'arquivo']