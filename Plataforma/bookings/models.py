from django.db import models

# Create your models here.

# class Reserva:
#
#     def __init__(self, nombre_de_usuario, destino):
#         self.nombre_de_usuario = nombre_de_usuario
#         self.destino = destino
# 
#     def __str__(self):
#         return f"Esta es una reserva de {self.nombre_de_usuario} con destino a {self.destino}"


class Reserva(models.Model):
    nombre_de_usuario = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)

    def __str__(self):
        return f"Esta es una reserva de {self.nombre_de_usuario} con destino a {self.destino}"