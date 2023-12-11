from django.shortcuts import redirect, render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Assiduidade, verify_email,CustomUser,Curso, obter_polo_por_curso , verificar_palavra_passe, Upload_Assiduidade,Polo
from django.contrib.auth import authenticate, login, logout





@login_required
def Dashboard(request):
    if request.method == "GET":
        user = request.user
        #Users=CustomUser.objects.get(curso = user.curso)
        Users=CustomUser.objects.all()
        if request.user.is_authenticated and request.user:#and request.user.groups.filter(name='Admin').exists():
            return render(request, 'G_Estagios/dashboard.html',({ 'customusers': Users, 'user':user}))


def submeter_docs(request):
    if request.method == 'GET':
        return render(request, 'G_Estagios/documentosAlunoCC.html')
    
def addicionar_Polo(request):
    pass

@login_required
def View_DocAluno(request):
    if request.methtod == 'GET':
         return render(request, 'G_Estagios/Aluno/documentos.html')

@login_required
def f_Registo(request):
    user=request.user
    if request.method == "GET":
        if user.is_completed == 1:
            return HttpResponseRedirect(reverse('dash'))
        else:
            curso = Curso
            cursos=curso.objects.all()
            return render(request,'G_Estagios/Finalizar_Registo.html',({'cursos':cursos}))
        
    elif request.method == 'POST':
        id_curso = request.POST.get('Curso')
        id_escola = obter_polo_por_curso(id_curso)
        escola = Polo.objects.get(id=id_escola)
        nome_escola = escola.nome
        curso= Curso.objects.get(id=id_curso)
        nome_curso = curso.nome_curso
        user.curso = nome_curso
        user.escola = nome_escola
        user.is_completed = True
        user.save()
        return HttpResponseRedirect(reverse('dash'),{'user':user})


def registo(request):
    if request.method == "GET":
        return render(request,'G_Estagios/Register.html')
    if request.method == "POST":
        User=CustomUser
        Email= request.POST.get('Email')
        try:
            V_Email = User.objects.get(username=Email)
        except User.DoesNotExist:
            V_Email = False
        if V_Email:
            messages.error(request,"Já existe um utilizador com esse email")
            return HttpResponseRedirect(reverse('registo'))
        else:
            Password=request.POST.get('Password')        
            Nome = request.POST.get('Nome')
            V_e = verify_email(Email)
            v_Password = verificar_palavra_passe(Password)
            if v_Password == False:
                messages.error(request,"Palavra-passe deve, pelo menos um caractere não alfabético, pelo menos uma letra maiúscula,Mínimo de 8 caracteres, pelo menos um número e pelo menos um caractere especial")
                return HttpResponseRedirect(reverse('registo'))
            elif v_Password == True:
                if V_e == "Invalido":
                    messages.error(request, 'Email invalido')
                    return HttpResponseRedirect(reverse('registo'))
                elif V_e == 'Aluno':
                    newuser = User.objects.create_user(username=Email,first_name=Nome,password=Password,privilegio=V_e,is_professor=False)
                    newuser.save()
                    messages.info(request,"Registo bem sucedido")
                    return HttpResponseRedirect(reverse('registo'))
                elif V_e == 'Professor':
                    newuser = User.objects.create_user(username=Email,first_name=Nome,password=Password,privilegio=V_e,is_professor=True,is_completed = True)
                    newuser.save()
                    messages.success(request,"Registo bem sucedido")
                    return HttpResponseRedirect(reverse('registo'))

def edit_user_admin(request):
    pass


def verificar_tipo_arquivo(arquivo):
    # Obtém a extensão do arquivo
    extensao = arquivo.name.split('.')[-1].lower()

    # Mapeia extensões conhecidas para tipos de arquivo
    tipos_permitidos = {
        'pdf': 'pdf',
        'docx': 'docx',
    }

    # Verifica se a extensão é permitida
    if extensao in tipos_permitidos:
        return tipos_permitidos[extensao]
    else:
        return None

def add_Assiduidade(request):
    if request.method == 'POST':
        arquivo = request.FILES.get('arquivo')

        if arquivo:
            # Verifique o tipo de arquivo
            tipo_arquivo = verificar_tipo_arquivo(arquivo)

            if tipo_arquivo in ['pdf', 'docx']:
                # Aqui você pode chamar a função Upload_Assiduidade
                # Certifique-se de passar os parâmetros necessários
                id_aluno = request.POST['id']
                Upload_Assiduidade(request,id_aluno)
                return HttpResponse("Upload bem-sucedido!")
            else:
                return HttpResponse("Tipo de arquivo inválido. Por favor, envie um PDF ou DOCX.")
    return render(request, 'G_Estagios/dashoard.html')


def view_login(request):
    if request.method == "GET":
        return render(request,'G_Estagios/Login.html')
    if request.method == 'POST':
        Username = request.POST["username"]
        Password = request.POST["password"]
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            login(request, user)
            user = request.user
            completo = user.is_completed
            if completo == True:
                # Redirecione para uma página de sucesso.
                return HttpResponseRedirect(reverse ('dash'))
            elif completo == False:
                return HttpResponseRedirect(reverse('finalizar_registo'))
        else:
            # Retorne uma mensagem de erro de 'login inválido'.
            messages.error(request,"Endereço de email ou password invalidos")
            return redirect('login')


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home'))


def Home(request):
    if request.method =='GET':
        return render(request,'G_Estagios/index.html')


def view_alunos_do_curso(request):
    # Recupere o usuário atualmente autenticado (coordenador de curso)
    coordenador = CustomUser.objects.get(username=request.user.username)

    # Recupere todos os alunos associados ao curso do coordenador
    alunos_do_curso = CustomUser.objects.filter(curso=coordenador.curso)

    # Renderize a página com a lista de alunos
    return render(request, 'alunos_do_curso.html', {'alunos': alunos_do_curso})


def mostrar_assiduidades(request, id_aluno, id_estagio):
    # Obtenha as assiduidades filtradas com base no usuário e no estágio
    assiduidades = Assiduidade.objects.filter(id_Aluno=id_aluno, id_Estagio=id_estagio)
    
    # Renderize a página com as assiduidades
    return render(request, 'mostrar_assiduidades.html', {'assiduidades': assiduidades})


def alter_user(request):
    if request.method == 'GET':
        return render(request,'G_Estagios/alteruser.html')
    if request.method == 'POST':
        novo_nome = request.POST.get('novo_nome')
        Password = request.POST.get('password')
        v_pass= verificar_palavra_passe(Password)
        if v_pass == False:
            messages.error(request,"Palavra-passe deve, pelo menos um caractere não alfabético, pelo menos uma letra maiúscula,Mínimo de 8 caracteres, pelo menos um número e pelo menos um caractere especial")
            return HttpResponseRedirect(reverse('registo'))
        elif v_pass == True:
            # Obtenha o usuário atual
            user = request.user
            # Faça as alterações necessárias
            user.first_name = novo_nome
            user.password = Password
            # Salve as alterações no banco de dados
            user.save()
            messages.success(request, 'As informações foram atualizadas com sucesso!')
        