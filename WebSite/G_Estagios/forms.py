from django import forms
from .models import *

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome_curso', 'Polo']
        widgets = {
            'nome_curso': forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
            'Polo': forms.Select(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}), 
            }
class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = ['tipo', 'arquivo']
        widgets = {
            
        }
class EstagioForm(forms.ModelForm):
    class Meta:
        model = Estagio
        fields = ['horas_totais', 'id_aluno', 
                  'id_cordenador_curso', 'id_tutor_estagio_escolar', 
                  'id_curso', 'Ano_Letivo', 'id_Empresa', 
                  'Assiduidade', 'id_Protocolos', 'id_Tutor_empresa']
        widgets = {
            'id_aluno': forms.Select(attrs = {'class':'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),   
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adicione personalizações ou widgets aqui, se necessário
        
        