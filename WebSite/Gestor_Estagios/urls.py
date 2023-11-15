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
    path('',views.starting, name='home'),
    path('Register/',views.Register, name='Register'),
    #path('Register/C_Register',views.f_Registo , name="finalizar_registo"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/',views.D_V, name='dash'),
]