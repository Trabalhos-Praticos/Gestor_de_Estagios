from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

#com api
import os
from dotenv import load_dotenv
import supabase
from supabase import create_client, Client
from .supabase import supa

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
        data = supa.auth.sign_in_with_password({"email": email, "password": password})
        loggedin = supa.auth.get_user()
        if loggedin:
            return HttpResponseRedirect(reverse('dash'))
        
@app.get("sign_out/")
def sign_out():
  supa = init_supabase()
  res = supa.auth.sign_out()
  return "success"
        
                
                

    
    
