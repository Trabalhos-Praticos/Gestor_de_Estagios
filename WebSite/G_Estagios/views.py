from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from .models import verify_email,CustomUser,Curso
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib.auth.models import Group


#com api
import os
from dotenv import load_dotenv
from supabase import create_client, Client
url = "https://rxpmviaksgbicuyrxqtr.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ4cG12aWFrc2diaWN1eXJ4cXRyIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5OTg2OTkwMywiZXhwIjoyMDE1NDQ1OTAzfQ.vE4o4iq3Y9bMPEcP8WFLlEVy6oUyqg7JhDLoK9hAOYI"
supabase: Client = create_client(url,key)

def starting(request):
    if request.method == "GET":
        return render(request,'G_Estagios/index.html')
    if request.method=='POST':
        # Sign in using the user email and password.
        email: str = request.POST.get['email']
        password: str = request.POST.get['password']
        user = supabase.auth.sign_in_with_password({ "email": email, "password": password })
        if user:
            return HttpResponse('Registado')

def Register(request):
    if request.method == "GET":
        return render(request,'G_Estagios/login_register_v001.html')
    if request.method == 'POST':
        email = request.POST.get('username') 
        password = request.POST.get('password')
        nome = request.POST.get('nome')
        res = supabase.auth.sign_up({ email,password })
        #data = supabase.auth.sign_in_with_password({"email": email, "password": password})
        return HttpResponse("registado",res)
#sem api



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
    

def Login(request):
    if request.method == "GET":
        return render(request,'G_Estagios/login_register_v001.html')



def autenticate(request):
    url: str = os.environ.get("SUPABASE_TEST_URL")
    key: str = os.environ.get("SUPABASE_TEST_KEY")
    supabase: Client = create_client(url, key)
    # Create a random user login email and password.
    email: str = request.POST.get['email']
    password: str = request.POST.get['password']
    user = supabase.auth.sign_up({ "email": email, "password": password })

#def register(request):
#    User=CustomUser
#    Email= request.POST.get('Email')
#    try:
#        V_Email = User.objects.get(username=Email)
#    except User.DoesNotExist:
#        V_Email = False
#    if V_Email:
#        return HttpResponse("Já existe um utilizador com esse email.")
#    else:
#        #confirmation_code = send_confirmation_email(Email)
#        Password=request.POST.get('Password')
#        Nome = request.POST.get('Nome')
#        V_e= verify_email(Email)
#        if V_e == "Invalido":
#            messages.error(request, 'Email invalido')
#            return render(request, 'Registo_Users/login.html')
#        elif V_e == 'Aluno':
#            newuser = User.objects.create_user(username=Email,first_name=Nome,password=Password)
#            newuser.save()
#            mensagem = "User registado com sucesso"
#            contexto = {'mensagem': mensagem}
#            return render(request,'G_Estagios/login_register_v001.html', contexto)
#        elif V_e == 'Professor':
#            newuser = User.objects.create_user(username=Email,first_name=Nome,password=Password)
#            newuser.save()
#            newuser.groups.add(name='Professor')
#            return render(request,'G_Estagios/login_register_v001.html')

def login_view(request):
    
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
    
def logout_view(request):
    logout(request)
    return render(request,'Registo_Users/registo.html')



