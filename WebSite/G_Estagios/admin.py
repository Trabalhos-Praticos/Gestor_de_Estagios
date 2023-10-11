from django.contrib import admin
from .models import CustomUser, Assiduidade,Estagio,Empresa,Curso,Polo,Protocolos

admin.site.register(CustomUser)
admin.site.register(Assiduidade)
admin.site.register(Estagio)
admin.site.register(Empresa)
admin.site.register(Curso)
admin.site.register(Polo)
admin.site.register(Protocolos)
