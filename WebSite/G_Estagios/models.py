from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    curso = models.CharField(max_length=100)
    escola = models.CharField(max_length=100)
    morada = models.CharField(max_length=255)
    privilegio = models.CharField(max_length=20)



class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nome_curso= models.CharField(max_length=70)
class Empresa(models.Model):
    id= models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120)

class Estagio(models.Model):
    id = models.AutoField(primary_key=True)
    horas_totais = models.IntegerField()
    id_aluno = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #id_cordenador_curso = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    #id_Tuto_estagio_escolar = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    Ano_Letivo = models.CharField(max_length=9)
    id_Empresa = models.ForeignKey(Empresa,on_delete=models.CASCADE)
    #id_Tutor_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    
    
#class Assiduidade(models.models):
#   pass

    

def verify_email(Email):
    # Validação de email
    if Email.endswith('@estg.ipvc.pt' or '@ese.ipvc.pt' or '@esa.ipvc.pt' or '@ess.ipvc.pt' or '@esce.ipvc.pt' or '@esdl.ipvc.pt'):
        return 'Professor'
    if Email.endswith('@ipvc.pt'):
        return 'Aluno'
    elif not Email.endswith('ipvc.pt'):
        return 'Invalido'


