from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import verify_email,CustomUser,Curso, verificar_palavra_passe,FormRegisto
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth.models import Group




@login_required
def D_v(request):
    if request.method == "GET":
        Users=CustomUser.objects.all()
        curso=Curso
        cursos=curso.objects.all()
        if request.user.is_authenticated:#and request.user.groups.filter(name='Admin').exists():
            return render(request, 'G_Estagios/dashboard.html',({'cursos': cursos, 'customusers': Users}))


@login_required
def f_Registo(request):
    if request.method == "GET":
        return render(request,'G_Estagios/Finalizar_Registo.html')
    elif request.method == 'POST':
        user=request.user
        user = user.objects.get(id=user.id)
        return HttpResponseRedirect(reverse('dash'))


def Register(request):
    if request.method == "GET":
        return render(request,'G_Estagios/Register.html')


def registo(request):
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
            newuser = User.objects.create_user(username=Email,first_name=Nome,password=Password)
            newuser.save()
            messages.info(request,"Registo bem sucedido")
            return redirect('register')
        elif V_e == 'Professor':
            newuser = User.objects.create_user(username=Email,first_name=Nome,password=Password)
            newuser.save()
            messages.success(request,"Registo bem sucedido")
            return redirect('register')

def registo_form(request):
    if request.method == 'POST':
        form = FormRegisto(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['password']
            # Verificar a segurança da palavra-passe
            is_password_secure, error_message = verificar_palavra_passe(senha)
            if is_password_secure:
                user = CustomUser(username=email,first_name = nome)
                user.set_password(senha)
                user.save()
                return redirect('pagina_sucesso')
            else:
                form.add_error('password', error_message)  # Adicione a mensagem de erro ao formulário
    else:
        form = FormRegisto()
    return render(request, 'G_Estagios/Register.html', {'form': form})
    
    
    
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