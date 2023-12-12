from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django import forms
from password_strength import PasswordPolicy
# Create your models here.



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
    ano = models.IntegerField(blank=True, default=1)



#Função que guarda o upload feito
def Upload_Assiduidade(request, id_aluno):
    if request.method == 'POST' and request.FILES['arquivo']:
        arquivo_enviado = request.FILES['arquivo']
        data_publicacao = timezone.now().strftime("%Y%m%d%H%M%S")
        nome_arquivo = f"{data_publicacao}_aluno{id_aluno}_assiduidade_{arquivo_enviado.name}"
        # Guarda o arquivo no sistema de arquivos
        fs = FileSystemStorage(location='Documentos/Assiduidade/')
        filename = fs.save(nome_arquivo, arquivo_enviado)
        # Cria uma nova instância de Assiduidade associada ao aluno correspondente
        assiduidade = Assiduidade.objects.create(id_Aluno=id_aluno, File=nome_arquivo)
        assiduidade.save()
        return assiduidade

class Protocolos(models.Model):
    id=models.AutoField(primary_key=True)
    File = models.FileField(upload_to='Documentos/Protocolos/',blank=True)
    data=models.DateField(auto_created=True,blank=True)
    id_Aluno=models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)


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
def Add_Curso(request):
    pass
class Empresa(models.Model):
    id= models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120,blank=True)
    def __str__(self):
        return self.nome_curso
class Assiduidade(models.Model):
    id=models.AutoField(primary_key=True)
    data=models.DateField(auto_created=True,blank=True)
    id_Aluno=models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    File = models.FileField(upload_to='Documentos/Assiduidade/',blank=True)
    

    
class Estagio(models.Model):
    id = models.AutoField(primary_key=True)
    horas_totais = models.IntegerField(blank=True)
    id_aluno = models.ForeignKey(CustomUser, related_name='estagios_aluno', on_delete=models.DO_NOTHING)
    id_cordenador_curso = models.ForeignKey(CustomUser, related_name='estagios_coordenador', on_delete=models.DO_NOTHING)
    id_tutor_estagio_escolar = models.ForeignKey(CustomUser, related_name='estagios_tutor', on_delete=models.DO_NOTHING)
    id_curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    Ano_Letivo = models.CharField(max_length=9,blank=True)
    id_Empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    Assiduidade = models.ForeignKey(Assiduidade, on_delete=models.DO_NOTHING)
    id_Protocolos=models.ForeignKey(Protocolos, on_delete=models.DO_NOTHING)
    id_Tutor_empresa = models.ForeignKey(Empresa, related_name='tutor_Empresa',on_delete=models.DO_NOTHING)

    

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

