from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import verify_email,CustomUser,Curso
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth.models import Group




@login_required
def D_v(request):
    # user = request.user
    # is_aluno = user.groups.filter(name='Alunos').exists()
    # is_professor = user.groups.filter(name='Professores').exists()
    
    # context = {
    #     'is_aluno': is_aluno,
    #     'is_professor': is_professor,
    #     'user_name': user.first_name  # Nome do usuário
    # }
    if request.method == "GET":
        Users=CustomUser.objects.all()
        curso=Curso
        cursos=curso.objects.all()
        return render(request, 'G_Estagios/users.html',({'cursos': cursos, 'customusers': Users}))
    
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

def login(request):
    if request.method == "GET":
        return render(request,'G_Estagios/login_register_v001.html')
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirecione para uma página de sucesso.
            return HttpResponseRedirect(reverse('dash'))

        else:
            # Retorne uma mensagem de erro de 'login inválido'.
            return HttpResponse("Email e/ou palavrapasse incorretas.")

@login_required
def logout_view(request):
    logout(request)
    return render(request,'G_Estagios/index.html')

def Home(request):
    if request.method =='GET':
        return render(request,'G_Estagios/index.html')