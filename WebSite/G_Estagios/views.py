from datetime import datetime
from django.shortcuts import redirect, render, HttpResponseRedirect,get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from .models import verify_email,CustomUser,Curso, obter_polo_por_curso , verificar_palavra_passe,Polo,Estagio
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib.auth.hashers import make_password
from django.http import FileResponse, HttpResponse


def Home(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponseRedirect(reverse('dash'))
    
    return render(request,'G_Estagios/index.html')


#def Dashboard(request):
#    user = request.user
#    current_page = None
#    estagio = None
#    if user.is_Coordenador_Curso:
#        try:
#            # Tente obter o objeto Estagio
#            estagio = Estagio.objects.get(id_cordenador_curso=user.id)
#            status_documentos = verifica_documentos_estagio(estagio)
#            Users=CustomUser.objects.filter(curso=user.curso)
#            # Número de pessoas a serem exibidas por página
#            pessoas_por_pagina = 10
#
#            # Inicialize o paginador com a lista de pessoas e o número de pessoas por página
#            paginator = Paginator(estagio, pessoas_por_pagina)
#
#            # Obtenha o número da página da solicitação. Se não houver número de página, use 1.
#            page = request.GET.get('page', 1)
#
#            try:
#                # Obtenha a página atual
#                current_page = paginator.page(page)
#            except PageNotAnInteger:
#                # Se a página não for um número inteiro, vá para a primeira página
#                current_page = paginator.page(1)
#            except EmptyPage:
#                # Se a página estiver vazia, vá para a última página
#                current_page = paginator.page(paginator.num_pages)
#        except Estagio.DoesNotExist:
#            return render(request, 'G_Estagios/dashboard.html', {'current_page': current_page,'user':user, 'estagios':estagio})
#    return render(request, 'G_Estagios/dashboard.html', {'current_page': current_page,'alunos':Users,'user':user, 'status_documento':status_documentos})

def get_alertas(request):
    user = request.user
    usercurso= Curso.objects.get(id=user.curso)
    alertas = Alertas.objects.filter(curso = user.curso)

def Dashboard(request):
    user = request.user
    #alerta = get_alertas(request)
    if user.is_Coordenador_Curso:
        #Tente obter o objeto Estagio
        estagios = Estagio.objects.filter(id_cordenador_curso=user.id)
        # status_documentos = verifica_documentos_estagio(estagio
         # Faça algo adequado se o Estagio não for encontrado

        # Obtenha a lista de usuários para paginar
        Users = CustomUser.objects.filter(curso=user.curso)

        # Número de pessoas a serem exibidas por página
        pessoas_por_pagina = 3

        # Inicialize o paginador com a lista de pessoas e o número de pessoas por página
        paginator = Paginator(Users, pessoas_por_pagina)

        # Obtenha o número da página da solicitação. Se não houver número de página, use 1.
        page = request.GET.get('page', 1)

        try:
            # Obtenha a página atual
            current_page = paginator.page(page)
        except PageNotAnInteger:
            # Se a página não for um número inteiro, vá para a primeira página
            current_page = paginator.page(1)
        except EmptyPage:
            # Se a página estiver vazia, vá para a última página
            current_page = paginator.page(paginator.num_pages)

        return render(request, 'G_Estagios/dashboard.html', {'current_page': current_page, 'alunos': Users, 'user': user, 'estagios': estagios})
    
    return render(request, 'G_Estagios/dashboard.html')
    
      
      
      
      
def verifica_documentos_estagio(estagio):
    # Obtém o mês atual
    mes_atual = datetime.now().strftime('%b').lower()

    # Verifica se existem documentos para o mês atual
    protocolo_presente = estagio.documentos.filter(tipo='protocolo', mes=mes_atual).exists()
    cv_presente = estagio.documentos.filter(tipo='cv', mes=mes_atual).exists()
    assiduidade_presente = estagio.documentos.filter(tipo='assiduidade', mes=mes_atual).exists()

    if protocolo_presente and cv_presente and assiduidade_presente:
        return True
    else: 
        return False
    
    
    
    
def pagina_404_personalizada(request, exception):
    return render(request, 'G_Estagios/404.html', status=404)    



def registo(request):
    curso = Curso.objects.all()
    if request.method == "POST":
        User=CustomUser
        Email= request.POST.get('username')
        try:
            V_Email = User.objects.get(username=Email)
        
        except User.DoesNotExist:
        
            V_Email = False
        
        if V_Email:
        
            messages.error(request,"Já existe um utilizador com esse email")
            return HttpResponseRedirect(reverse('registo'))
        
        else:
            id_curso = request.POST.get('curso')
            id_escola = obter_polo_por_curso(id_curso)
            Escola = Polo.objects.get(id=id_escola)
            f_Curso= Curso.objects.get(id=id_curso)
            Password=request.POST.get('password')        
            primeiro_Nome = request.POST.get('pnome')
            ultimo_nome = request.POST.get('unome')
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
           
                    newuser = User.objects.create_user(username=Email,first_name=primeiro_Nome,last_name=ultimo_nome,password=Password,privilegio=V_e,curso=f_Curso,escola = Escola,is_completed = True)
                    newuser.save()
                    messages.info(request,"Registo bem sucedido")
                    return HttpResponseRedirect(reverse('registo'))
           
                elif V_e == 'Professor':
           
                    newuser = User.objects.create_user(username=Email,first_name=primeiro_Nome,last_name=ultimo_nome,password=Password,privilegio=V_e,is_professor=True,is_completed = True)
                    newuser.save()
                    messages.success(request,"Registo bem sucedido")
           
                    return HttpResponseRedirect(reverse('registo'))
                
                
    return render(request,'G_Estagios/Register.html',{'cursos':curso})



def f_Registo(request):
    user=request.user
    
    if user.is_completed == 1:
        return HttpResponseRedirect(reverse('dash'))
    
    elif request.method == 'POST':
        id_curso = request.POST.get('Curso')
        id_escola = obter_polo_por_curso(id_curso)
        escola = Polo.objects.get(id=id_escola)
        curso= Curso.objects.get(id=id_curso)
        user.curso = curso.id
        user.escola = escola.id
        user.is_completed = True
        user.save()
        return HttpResponseRedirect(reverse('dash'),{'user':user})
    else:
        curso = Curso
        cursos=curso.objects.all()
        return render(request,'G_Estagios/Finalizar_Registo.html',({'cursos':cursos})) 
    
    




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
    


def view_login(request):
   
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
                messages.success(request,"Login bem sucedido")    
                return HttpResponseRedirect(reverse ('dash'))
   
            elif completo == False:
                return HttpResponseRedirect(reverse('finalizar_registo'))
   
        else:
   
            # Retorne uma mensagem de erro de 'login inválido'.
            messages.error(request,"Endereço de email ou password invalidos")
            return redirect('login')
     
    return render(request,'G_Estagios/Login.html')



def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('Home'))



def view_alunos_do_curso(request):
    # Recupere o usuário atualmente autenticado (coordenador de curso)
    coordenador = CustomUser.objects.get(username=request.user.username)

    # Recupere todos os alunos associados ao curso do coordenador
    alunos_do_curso = CustomUser.objects.filter(curso=coordenador.curso)

    # Renderize a página com a lista de alunos
    return render(request, 'alunos_do_curso.html', {'alunos': alunos_do_curso})



def alter_user(request,user_id):
    user = CustomUser.objects.get(pk=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user.password = make_password(user.password)
            form.save()
            return HttpResponseRedirect(reverse('dash'))
    else:
        form = CustomUserChangeForm(instance=user)
    
    return render(request,'G_Estagios/editarperfil.html',{'form':form,'user':user})


def view_polo_curso(request):
    user = request.user
    cursos = Curso.objects.all()
    Polos = Polo.objects.all()
    if user.is_superuser == 0:
        return HttpResponseRedirect(reverse('dash'))
    return render(request,'G_Estagios/administracao/CRUDcurso__e_escola.html',{'cursos':cursos , 'Polos':Polos })


def submeter_docs(request):
    user = request.user
    try:
        estagio  = Estagio.objects.get(id_aluno=user.id)
    except Estagio.DoesNotExist:
        messages.error(request,'Não Podes submeter ficheiros enquanto não estiveres com um estagio associado, contacta o teu coordenador de curso')
        return HttpResponseRedirect(reverse('dash'))
    
    if request.method == 'POST':
        form = DocumentoForm(request.POST, request.FILES)
        if form.is_valid():
            documento = form.save(commit=False)
            documento.usuario = request.user
            documento.estagio = estagio
            documento.save()
            return HttpResponseRedirect(reverse('sub_docs'))  # ou a página desejada após adicionar o documento
    else:
        form = DocumentoForm()
    
    
    return render(request, 'G_Estagios/documentos.html', {'form': form})
    
    
    



def View_DocAluno(request):
    if request.methtod == 'GET':
         return render(request, 'G_Estagios/Aluno/documentos.html')


#Funções para o Admin

def create_curso(request):
    user = request.user
    if user.is_superuser == 0:
        return HttpResponseRedirect(reverse('dash'))
    if request.method == 'POST':
        curso = Curso
        curso_nome = request.POST['nome']
        curso_polo = request.POST['polo']
        polo = Polo.objects.get(id=curso_polo)
        new_curso = curso.objects.create(nome_curso=curso_nome, Polo=polo)
        new_curso.save()
        messages.success(request,'Curso criado e associado com sucesso.')   
        return HttpResponseRedirect(reverse('polo_curso'))




def eliminar_curso(request, curso_id):
    user = request.user
    if user.is_superuser == 0:
        return HttpResponseRedirect(reverse('dash'))
    if request.method == 'POST':
        curso = get_object_or_404(Curso, id=curso_id)
        curso.delete()
        messages.success(request,'Curso eliminado com sucesso.')
        return HttpResponseRedirect(reverse('polo_curso'))      



def editar_curso(request, curso_id):
    user = request.user
    if user.is_superuser == 0:
        return HttpResponseRedirect(reverse('dash'))
    
    curso = get_object_or_404(Curso, id=curso_id)
    polos = Polo.objects.all()
    
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request,'Curso editado com sucesso')
            return HttpResponseRedirect(reverse('polo_curso'))
    else:
        form = CursoForm(instance=curso)
    return render(request, 'G_Estagios/administracao/editarCurso.html', {'form': form, 'curso': curso,'polos':polos})


def alertas(request):
    return render(request,'G_Estagios/Alertas/alertas.html')



def create_polo(request):
    user = request.user
    if user.is_superuser == 0:
        return HttpResponseRedirect(reverse('dash'))
    if request.method == 'POST':
            polo = Polo
            nome_polo = request.POST['nome']
            new_polo = polo.objects.create(nome=nome_polo)
            
            new_polo.save()
            
            messages.success(request,'Escola criada com sucesso.')
            return HttpResponseRedirect(reverse('polo_curso'))




def admin_user(request):
    users = CustomUser.objects.all()
    return render(request,'G_Estagios/administracao/Registo_aluno.html',{'users':users})



def eliminar_polo(request, polo_id):
    user = request.user
    if user.is_superuser == 0:
        return HttpResponseRedirect(reverse('dash'))
    if request.method == 'POST':
        polo = get_object_or_404(Polo, id=polo_id)
        polo.delete()
        return HttpResponseRedirect(reverse('polo_curso'))

def edit_user_admin(request):
    user = request.user
    if request.method == 'POST':
        pass
    
def adm_panel(request):
    user = request.user
    if user.is_superuser == 0:
        return HttpResponseRedirect(reverse('dash'))
    return render(request,'G_Estagios/administracao/adm_panel.html')



def empresa_view(request):
    empresas = Empresa.objects.all()
    if request.method == 'POST':
        nome_ = request.POST['nome']
        loc = request.POST['loc']
        empresa = Empresa.objects.create(nome = nome_, localizacao=loc)
        empresa.save()
        messages.success(request,'Empresa adicionada com sucesso.')
        return HttpResponseRedirect(reverse('empresa_view'))
    return render(request,'G_Estagios/Empresa/Empresas.html',{'empresas':empresas})



def alter_empresa(request, id_empresa):
    empresa = get_object_or_404(Empresa, pk=id_empresa)

    if request.method == 'POST':
        # Se os dados do formulário foram enviados
        empresa.nome = request.POST['nome']
        empresa.localizacao = request.POST['loc']
        # Adicione outros campos conforme necessário
        empresa.save()
        messages.success(request, 'Empresa com o ID {} editada com sucesso.'.format(empresa.id))
        # Redirecione para a página de detalhes da empresa ou qualquer outra página desejada
        return HttpResponseRedirect(reverse('empresa_view'))
    else:
        # Se é uma solicitação GET, renderize o formulário com os dados atuais
        return render(request, 'G_Estagios/Empresa/alterar_empresa.html', {'empresa': empresa})


#estagio
def painel_estagios(request):
    user = request.user
    # Obter a lista de IDs dos alunos que têm um estágio
    alunos_com_estagio_ids = Estagio.objects.values_list('id_aluno_id', flat=True)

    # Obter a lista de todos os alunos do mesmo curso do usuário
    alunos_mesmo_curso = CustomUser.objects.filter(privilegio='Aluno', curso=user.curso)

    # Filtrar os alunos que não têm um estágio e pertencem ao mesmo curso do usuário
    alunos = alunos_mesmo_curso.exclude(id__in=alunos_com_estagio_ids)
    
    
    CC = CustomUser.objects.filter(is_Coordenador_Curso = True)
    TTES = CustomUser.objects.filter(is_Tutor_estagio_Escola = True)
    emp = Empresa.objects.all()
    curso = Curso.objects.all()
    estagios = Estagio.objects.all()
    try:
        estagio = Estagio.objects.get(id_aluno=user.id)
    except Estagio.DoesNotExist:
        # Lógica a ser executada se não houver nenhum resultado
        return render(request,'G_Estagios/Estagio/estagioCC.html',{'alunos':alunos,'ccs':CC,'TTS':TTES,'emp':emp,'curso':curso})
    return render(request,'G_Estagios/Estagio/estagioCC.html',{'alunos':alunos,'ccs':CC,'TTS':TTES,'emp':emp,'curso':curso,'estagio':estagio,'estagios':estagios})


def adicionar_estagi(request):
    if request.method == 'POST':
            # Processar dados do formulário para adicionar estágio
            horas_totais = request.POST.get('HT')
            id_aluno = request.POST.get('AL')
            id_cc = request.POST['CC']
            id_TE = request.POST['TE']#id tutor estagio
            empresa = request.POST['EMP']
            curso = request.POST['curso']
            ano_letivo = definir_ano_letivo()
             
            tutor_estagio_escolar = get_object_or_404(CustomUser, id=id_TE)
            coordenador_curso = get_object_or_404(CustomUser, id=id_cc)
            empresa = get_object_or_404(Empresa, id=empresa)
            nCurso = get_object_or_404(Curso, id=curso)
            # Criar instância de Estagio
            estagio = Estagio.objects.create(
                Ano_Letivo = ano_letivo,
                id_aluno_id=id_aluno,
                id_cordenador_curso =coordenador_curso,id_Empresa=empresa,
                id_tutor_estagio_escolar = tutor_estagio_escolar,
                horas_totais=horas_totais,id_curso=nCurso
            )
            estagio.save()
            messages.success(request,'Estagio criado com sucesso')
            return HttpResponseRedirect(reverse('painel_estagios'))
        
def excluir_estagio(request, id_estagio):
    estagio = get_object_or_404(Estagio, pk=id_estagio)
    # Confirmar exclusão (você pode adicionar lógicas adicionais aqui)
    estagio.delete()
    messages.success(request, 'Estágio excluído com sucesso.')
    return HttpResponseRedirect(reverse('painel_estagios'))  # Redirecione para a página que lista todos os estágios



def definir_ano_letivo():
    # Lógica para definir o ano letivo com base em algum critério
    # Por exemplo, você pode obter o ano atual e calcular o próximo ano letivo
    
    # Obter o ano atual
    ano_atual = datetime.now().year
    
    # Calcular o próximo ano letivo (assumindo que o ano letivo vai de setembro a agosto)
    if datetime.now().month >= 9:  # Se já passou setembro
        ano_letivo = f"{ano_atual}/{ano_atual + 1}"
    else:
        ano_letivo = f"{ano_atual - 1}/{ano_atual}"
    
    return ano_letivo

def perfil(request,user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    # Obtém informações sobre o estágio do usuário
    estagio = Estagio.objects.get(id_aluno=user.id)
    # Obtém todos os documentos do usuário
    documentos = Documento.objects.filter(usuario=user)

    
    return render(request,'G_Estagios/Alunos/perfil_Aluno.html', {'aluno': user,'estagio': estagio, 'documentos': documentos})


def download_documento(request, documento_id):
    # Obtém a instância do documento com base no ID
    documento = get_object_or_404(Documento, id=documento_id)

    # Lógica para obter o caminho do arquivo ou objeto File
    # Substitua isso com base na sua implementação específica
    caminho_do_arquivo = documento.arquivo.path
    try:
        # Abre o arquivo em modo binário e lê seu conteúdo
        with open(caminho_do_arquivo, 'rb') as arquivo:
            # Cria uma resposta HTTP com o conteúdo do arquivo
            response = HttpResponse(arquivo.read(), content_type='application/force-download')
            response['Content-Disposition'] = f'attachment; filename="{documento.nome_do_arquivo}"'

        # Redireciona para a página "painel_user"
        return redirect(reverse('painel_user'))

    except Exception as e:
        messages.error(request, 'Erro ao descaregar o arquivo.')
    return HttpResponseRedirect(reverse('painel_user'))