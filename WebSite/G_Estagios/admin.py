from django.contrib import admin
from .models import CustomUser,Estagio,Empresa,Curso,Polo

admin.site.register(CustomUser)
admin.site.register(Estagio)
admin.site.register(Empresa)
admin.site.register(Curso)
admin.site.register(Polo)

