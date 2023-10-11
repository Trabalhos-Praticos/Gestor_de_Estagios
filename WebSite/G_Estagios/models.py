from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
import secrets
import string
# Create your models here.



class CustomUser(AbstractUser):
    curso = models.CharField(max_length=100, blank=True)
    escola = models.CharField(max_length=100,blank=True)
    morada = models.CharField(max_length=255,blank=True)
    is_professor=models.BooleanField(default=False)
    is_Coordenador_Curso=models.BooleanField(default=False)
    is_Tutor_estagio_Empresa=models.BooleanField(default=False)
    is_Tutor_estagio_Escola= models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)
    privilegio = models.CharField(max_length=20,blank=True)
    confirmation_code= models.CharField(max_length=255)


class Assiduidade(models.Model):
    id=models.AutoField(primary_key=True)
    data=models.DateField(auto_created=True,blank=True)
    id_Aluno=models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    File = models.FileField(upload_to='Documentos/Assiduidade/',blank=True)
    

    
#Função que guarda o upload feito
def Upload_Assiduidade(request, id_aluno, id_assiduidade):
    if request.method == 'POST' and request.FILES['arquivo']:
        arquivo_enviado = request.FILES['arquivo']
        data_publicacao = timezone.now().strftime("%Y%m%d%H%M%S")
        nome_arquivo = f"{data_publicacao}_aluno{id_aluno}_assiduidade{id_assiduidade}_{arquivo_enviado.name}"

        fs = FileSystemStorage(location='Documentos/Assiduidade/')
        filename = fs.save(nome_arquivo, arquivo_enviado)

        # Salve o nome do arquivo na base de dados
        assiduidade = Assiduidade.objects.get(pk=id_assiduidade)
        assiduidade.nome_arquivo = nome_arquivo
        assiduidade.save()

def alteruser(request):
    pass

class Protocolos(models.Model):
    id=models.AutoField(primary_key=True)
    File = models.FileField(upload_to='Documentos/Protocolos/',blank=True)
    data=models.DateField(auto_created=True,blank=True)
    id_Aluno=models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)


#Função que guarda o upload feito
def Upload_Assiduidade(request, id_aluno, id_assiduidade):
    if request.method == 'POST' and request.FILES['arquivo']:
        arquivo_enviado = request.FILES['arquivo']
        data_publicacao = timezone.now().strftime("%Y%m%d%H%M%S")
        nome_arquivo = f"{data_publicacao}_aluno{id_aluno}_assiduidade{id_assiduidade}_{arquivo_enviado.name}"

        fs = FileSystemStorage(location='Documentos/Assiduidade/')
        filename = fs.save(nome_arquivo, arquivo_enviado)

        # Salve o nome do arquivo na base de dados
        assiduidade = Protocolos.objects.get(pk=id_assiduidade)
        assiduidade.nome_arquivo = nome_arquivo
        assiduidade.save()
        
class Polo(models.Model):
    id=models.AutoField(primary_key=True)
    nome=models.CharField(max_length=50)
def Add_Polo(request):
    pass
class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nome_curso= models.CharField(max_length=70,blank=True)
    Polo= models.ForeignKey(Polo,on_delete=models.DO_NOTHING)
def Add_Curso(request):
    pass
class Empresa(models.Model):
    id= models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120,blank=True)


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
    
    
#class Assiduidade(models.models):
#   pass

    

def verify_email(Email):
    # Validação de email
    if Email.endswith('@estg.ipvc.pt' or '@ese.ipvc.pt' or '@esa.ipvc.pt' or '@ess.ipvc.pt' or '@esce.ipvc.pt' or '@esdl.ipvc.pt'):
        return 'Professor'
    if Email.endswith('@ipvc.pt'):
        return 'Aluno'
    elif not Email.endswith('ipvc.pt'):
        return 'Externo'


#Gera ium codigo unico 
def generate_unique_confirmation_code():
    while True:
        characters = string.ascii_letters + string.digits
        confirmation_code = ''.join(secrets.choice(characters) for _ in range(20))
        
        # Verifique se o código já existe na base de dados
        if not CustomUser.objects.filter(confirmation_code=confirmation_code).exists():
            return confirmation_code

from django.core.mail import send_mail

def send_confirmation_email(Email):
    confirmation_code = generate_unique_confirmation_code()
    subject = 'Confirmação de Registro'
    message = f'Seja bem-vindo ao nosso site! Seu código de confirmação é: {confirmation_code}'
    from_email = 'esquilogpg2@gmail.com'
    recipient_list = [Email]
    send_mail(subject, message, from_email, recipient_list)
    return confirmation_code