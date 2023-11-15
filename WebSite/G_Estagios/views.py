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
import supabase
from supabase import create_client, Client

url = "https://rxpmviaksgbicuyrxqtr.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ4cG12aWFrc2diaWN1eXJ4cXRyIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5OTg2OTkwMywiZXhwIjoyMDE1NDQ1OTAzfQ.vE4o4iq3Y9bMPEcP8WFLlEVy6oUyqg7JhDLoK9hAOYI"
supabase_client = supabase.create_client(url, key)

def starting(request):
    if request.method == "GET":
        return render(request,'G_Estagios/index.html')

def Register(request):
    if request.method == "GET":
        return render(request,'G_Estagios/login_register_v001.html')
    if request.method == 'POST':
        email = request.POST.get('Email') 
        password = request.POST.get('Password')
        nome = request.POST.get('Nome')
        res = supabase_client.auth.sign_up({
            "email": email,
            "password": password,
            "options": {
                "data": {
                    "first_name": nome,
                }
            }
        })
        return HttpResponseRedirect(reverse('dash'))

def D_V(request):
    if request.method== 'GET':
        return render(request,"G_Estagios/coiso.html",)

def login_view(request):
    if request.method== 'GET':
        return render(request,"G_Estagios/login_register_v001.html",)
    if request.method== 'POST':
        email = request.POST.get('Email')
        password= request.POST.get('Password')
        data = supabase.auth.sign_in_with_password({"email": email, "password": password})
        if data:
            return HttpResponseRedirect(reverse('dash'))
        
def logout_view(request):
    
    token_de_sesso = request.COOKIES.get('token_de_sesso')
    
    if token_de_sesso is not None:
        # Faz logout usando Supabase
        response = supabase_client.auth.sign_out(token_de_sesso)

        # Verifica se o logout foi bem-sucedido
        if response is not None and response.get('error') is not None:
            print(f"Erro ao fazer logout: {response['error']}")
        else:
            response = supabase_client.auth.sign_out()
            print("Logout bem-sucedido!")
            # Faz logout usando Supabase
            # Verifica se o logout foi bem-sucedido
            if response.get('error') is not None:
                print(f"Erro ao fazer logout: {response['error']}")
            else:
                # Redireciona para a página inicial ou outra página após o logout
                return HttpResponseRedirect(reverse('login'))

    
    
