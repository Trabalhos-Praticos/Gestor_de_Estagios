
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from .models import Alertas

class VerificarAutenticacaoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Lista de páginas permitidas sem autenticação
        paginas_sem_autenticacao = ['/login/', '/registo/','/']

        if not request.user.is_authenticated and request.path_info not in paginas_sem_autenticacao:
            # Redireciona para a página de login se o usuário não estiver autenticado
            return HttpResponseRedirect(reverse('Home'))
        
        if request.path_info.startswith('/api/'):
            return self.get_response(request)
        
        response = self.get_response(request)
        return response
    
