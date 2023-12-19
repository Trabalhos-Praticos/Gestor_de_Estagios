from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django import forms
import schedule
import time
from password_strength import PasswordPolicy

class CustomUser(AbstractUser):
    curso = models.CharField(max_length=100, blank=True)
    escola = models.CharField(max_length=100,blank=True)
    morada = models.CharField(max_length=255,blank=True)
    is_professor=models.BooleanField(default=False)
    is_Coordenador_Curso=models.BooleanField(default=False)
    is_Tutor_estagio_Empresa=models.BooleanField(default=False)
    is_Tutor_estagio_Escola= models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    privilegio = models.CharField(max_length=20,blank=True)
    ano = models.IntegerField(blank=True, default=2)

class Documento(models.Model):
    TIPOS_DOCUMENTO = [
        ('protocolo', 'Protocolo'),
        ('cv', 'Currículo'),
        ('assiduidade', 'Assiduidade'),
        ('relatorio', 'Relatório'),
    ]
    
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPOS_DOCUMENTO)
    arquivo = models.FileField(upload_to='documentos/')

    def __str__(self):
        return f"{self.tipo} - {self.usuario.username}"



class Polo(models.Model):
    id=models.AutoField(primary_key=True)
    nome=models.CharField(max_length=50)
    def __str__(self):
        return self.nome
    
def obter_polo_por_curso(id_curso):
    curso = Curso.objects.get(id=id_curso)
    polo_associado = curso.Polo
    polo = Polo.objects.get(nome=polo_associado)
    return polo.id

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nome_curso= models.CharField(max_length=70,blank=True)
    Polo = models.ForeignKey(Polo,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.nome_curso

class Alertas(models.Model):
    id = models.AutoField(primary_key=True)
    Texto = models.TextField(blank=True)
    curso = models.TimeField(blank=True)

class Empresa(models.Model):
    id= models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120,blank=True)
    
    def __str__(self):
        return self.nome
    

class Estagio(models.Model):
    id = models.AutoField(primary_key=True)
    horas_totais = models.IntegerField(blank=True)
    id_aluno = models.ForeignKey(CustomUser, related_name='estagios_aluno', on_delete=models.DO_NOTHING)
    id_cordenador_curso = models.ForeignKey(CustomUser, related_name='estagios_coordenador', on_delete=models.DO_NOTHING)
    id_tutor_estagio_escolar = models.ForeignKey(CustomUser, related_name='estagios_tutor', on_delete=models.DO_NOTHING)
    id_curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    Ano_Letivo = models.CharField(max_length=9,blank=True)
    id_Empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    Assiduidade = models.ForeignKey(Documento,related_name='assiduidade', on_delete=models.DO_NOTHING)
    id_Protocolos=models.ForeignKey(Documento,related_name='protocolos', on_delete=models.DO_NOTHING)
    id_Tutor_empresa = models.ForeignKey(Empresa, related_name='tutor_Empresa',on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.nome
    

def verify_email(Email):
    # Validação de email
    if Email.endswith('@estg.ipvc.pt' or '@ese.ipvc.pt' or '@esa.ipvc.pt' or '@ess.ipvc.pt' or '@esce.ipvc.pt' or '@esdl.ipvc.pt'):
        return 'Professor'
    if Email.endswith('@ipvc.pt'):
        return 'Aluno'
    elif not Email.endswith('@ipvc.pt'):
        return 'Invalido'

    
def verificar_palavra_passe(palavra_passe):
    policy = PasswordPolicy.from_names(
        length=8,  # Mínimo de 8 caracteres
        uppercase=1,  # Pelo menos uma letra maiúscula
        numbers=1,  # Pelo menos um número
        special=1,  # Pelo menos um caractere especial
        nonletters=1,  # Pelo menos um caractere não alfabético
    )
    resultado = policy.test(palavra_passe)
    if resultado:
        return False
    else:
        return True  # Palavra-passe atende aos critérios




