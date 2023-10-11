from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import verify_email,CustomUser
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse





def Mainpage(request):
    if request.method == "GET":
        return render(request,'G_Estagios/login_register_v001.html')

def dashboard(request):
    if request.method == "GET":
        return render(request,'Registo_Users/dashboard.html')




def register(request):
    User=CustomUser
    Email= request.POST.get('Email')
    try:
        V_Email = User.objects.get(username=Email)
    except User.DoesNotExist:
        V_Email = False
    if V_Email:
        return HttpResponse("Já existe um utilizador com esse email.")
    else:
        #confirmation_code = send_confirmation_email(Email)
        Password=request.POST.get('Password')
        Nome = request.POST.get('Nome')
        V_e= verify_email(Email)
        if V_e == "Invalido":
            messages.error(request, 'Email invalido')
            return render(request, 'Registo_Users/login.html')
        newuser = User.objects.create_user(username=Email,first_name=Nome,password=Password)
        newuser.save()
        return HttpResponse('Parabens está registado')
    

def login_view(request):
    
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirecione para uma página de sucesso.
        return HttpResponse("logado")
        
    else:
        # Retorne uma mensagem de erro de 'login inválido'.
        return HttpResponse("Email e/ou palavrapasse incorretas.")
    
def logout_view(request):
    logout(request)
    return render(request,'Registo_Users/registo.html')



