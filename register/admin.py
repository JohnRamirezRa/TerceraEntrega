from django.contrib import admin
from register.models import Usuarios

# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display=("nombre", "apellido", "email", "clave")

admin.site.register(Usuarios, RegisterAdmin)