from django.db import models
from django.contrib.auth.models import AbstractUser
from password_strength import PasswordPolicy




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

class CustomUser(AbstractUser):
    curso = models.ForeignKey(Curso,on_delete=models.DO_NOTHING,blank = True)
    escola = models.ForeignKey(Polo,on_delete=models.DO_NOTHING,blank = True)
    morada = models.CharField(max_length=255,blank=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    is_Coordenador_Curso=models.BooleanField(default=False)
    is_Tutor_estagio_Empresa=models.BooleanField(default=False)
    is_Tutor_estagio_Escola= models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    privilegio = models.CharField(max_length=20,blank=True)



class Alertas(models.Model):
    id = models.AutoField(primary_key=True)
    Texto = models.TextField(blank=True)
    curso = models.TimeField(blank=True)
    id_user = models.ForeignKey(CustomUser, null= True ,related_name='user', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.id} - {self.id_user}"
    
class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=120,blank=True)
    localizacao = models.CharField(max_length=120,blank=True)
    def __str__(self):
        return self.nome
    

class Estagio(models.Model):
    id = models.AutoField(primary_key=True)
    horas_totais = models.IntegerField(blank=True)
    id_aluno = models.ForeignKey(CustomUser, related_name='estagios_aluno', on_delete=models.DO_NOTHING)
    id_cordenador_curso = models.ForeignKey(CustomUser, related_name='estagios_coordenador', on_delete=models.DO_NOTHING)
    id_tutor_estagio_escolar = models.ForeignKey(CustomUser, related_name='estagios_tutor', on_delete=models.DO_NOTHING)
    id_curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    Ano_Letivo = models.CharField(max_length=9, blank=True, null=True, help_text='Formato: YYYY/YYYY')
    id_Empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    documentos = models.ManyToManyField('Documento', related_name='Estagio', blank=True)
    id_Tutor_empresa = models.ForeignKey(Empresa, related_name='tutor_Empresa',on_delete=models.DO_NOTHING,blank = True, null = True)
    

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

class Documento(models.Model):
    TIPOS_DOCUMENTO = [
        ('protocolo', 'Protocolo'),
        ('cv', 'Currículo'),
        ('assiduidade', 'Assiduidade'),
        ('relatorio', 'Relatório'),
    ]
    
    MESES = [
        ('fev', 'Fevereiro'),
        ('mar', 'Março'),
        ('abr', 'Abril'),
        ('mai', 'Maio'),
        ('jun', 'Junho'),
        ('jul', 'Julho'),
        ('ago', 'Agosto'),
        # Adicione os outros meses conforme necessário
    ]

    usuario = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    estagio = models.ForeignKey('Estagio', on_delete=models.CASCADE, related_name='Documentos', null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPOS_DOCUMENTO)
    arquivo = models.FileField(upload_to='documentos/')
    
    # Campo adicional para o mês, só é usado quando o tipo é 'assiduidade'
    mes = models.CharField(max_length=3, choices=MESES, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.usuario.username}"



