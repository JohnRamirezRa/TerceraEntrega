from django.db import models

class Usuarios(models.Model):
    nombre=models.CharField(max_length=45)
    apellido=models.CharField(max_length=45)
    email=models.EmailField(max_length=100, blank=True, null=True)
    clave=models.CharField(max_length=45)

    def __str__(self) -> str:
        return f'El usuario {Usuarios.apellido} {Usuarios.nombre} Con correo {Usuarios.email} y contrasenia {Usuarios.clave}'