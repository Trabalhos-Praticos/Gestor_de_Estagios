"""
URL configuration for Gestor_Estagios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from G_Estagios import views



urlpatterns = [
    #rota,view,nome de referencia
    path('admin/', admin.site.urls),
    path('',views.Home, name='Home'),
    path('registo/',views.registo, name='registo'),
    path('Registo/f_r',views.f_Registo,name="finalizar_registo"),
    path('login/', views.view_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/',views.Dashboard, name='dash'),
    path('alunos-do-curso/', views.view_alunos_do_curso, name='alunos_do_curso'),
    path('Documentos/', views.submeter_docs, name="sub_docs"),
    path('Estagios/',views.painel_estagios,name='painel_estagios'),
    path('Estagios/criar/',views.adicionar_estagi,name='criar_estagio'),
    path('Estagios/editar/<int:id_estagio>/',views.editar_estagio,name='editar_estagio'),
    path('Estagios/eliminar/<int:id_estagio>/',views.excluir_estagio,name='excluir_estagio'),
    path('user/alterar_user/<int:user_id>/', views.alter_user, name='alterar_usuario'),
    path('empresa/',views.empresa_view,name='empresa_view'),
    path('empresa/alterar_empresa/<int:id_empresa>/',views.alter_empresa,name='empresa_alter'),
    path('administracao/escola_curso/',views.view_polo_curso,name='polo_curso'),
    path('administracao/escola_curso/CriarCurso',views.create_curso,name='criar_curso'),
    path('administracao/escola_curso/CriarEscola',views.create_polo,name='criar_polo'),
    path('administracao/painelAdm',views.adm_panel,name = 'admin'),
    path('administracao/escola_curso/eliminar_curso/<int:curso_id>/', views.eliminar_curso, name='eliminar_curso'),
    path('administracao/escola_curso/editar_curso/<int:curso_id>/', views.editar_curso, name='editar_curso'),
    path('administracao/escola_curso/eliminar_polo/<int:polo_id>/', views.eliminar_polo, name='eliminar_polo'),
    path('administracao/estudantes/',views.admin_user,name='painel_users'),
    
]
handler404 = 'G_Estagios.views.pagina_404_personalizada'