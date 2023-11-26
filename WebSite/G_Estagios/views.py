from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import verify_email,CustomUser,Curso, verificar_palavra_passe
from django.contrib.auth import authenticate, login, logout





@login_required
def D_v(request):
    if request.method == "GET":
        Users=CustomUser.objects.all()
        curso=Curso
        cursos=curso.objects.all()
        if request.user.is_authenticated and request.user:#and request.user.groups.filter(name='Admin').exists():
            return render(request, 'G_Estagios/dashboard.html',({'cursos': cursos, 'customusers': Users}))




@login_required
def f_Registo(request):
    if request.method == "GET":
        return render(request,'G_Estagios/Finalizar_Registo.html')
    elif request.method == 'POST':
        Curso = request.POST.get('Curso')
        user=request.user
        return HttpResponseRedirect(reverse('dash'))




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
            return redirect('register')
        else:
            Password=request.POST.get('Password')        
            Nome = request.POST.get('Nome')
            V_e = verify_email(Email)
            if V_e == "Invalido":
                messages.error(request, 'Email invalido')
                return redirect('register')
            elif V_e == 'Aluno':
                newuser = User.objects.create_user(username=Email,first_name=Nome,password=Password,privilegio=V_e,is_professor=False)
                newuser.save()
                messages.info(request,"Registo bem sucedido")
                return redirect('register')
            elif V_e == 'Professor':
                newuser = User.objects.create_user(username=Email,first_name=Nome,password=Password,privilegio=V_e,is_professor=True)
                newuser.save()
                messages.success(request,"Registo bem sucedido")
                return redirect('register')
    
def view_login(request):
    if request.method == "GET":
        return render(request,'G_Estagios/Login.html')
    if request.method == 'POST':
        Username = request.POST["username"]
        Password = request.POST["password"]
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            login(request, user)
            # Redirecione para uma página de sucesso.
            return HttpResponseRedirect(reverse ('dash'))
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