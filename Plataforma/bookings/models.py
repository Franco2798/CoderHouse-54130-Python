from django.db import models
from django.utils import timezone

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    capacidad = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {'Disponible' if self.disponible else 'No Disponible'} - Capacidad: {self.capacidad}"

class Reserva(models.Model):
    nombre_de_usuario = models.CharField(max_length=50)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='reservas')
    fecha = models.DateField(default=timezone.now)
    hora_inicio = models.TimeField(default=timezone.now)
    hora_fin = models.TimeField(default=timezone.now)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_de_usuario} - {self.sala.nombre} - {self.fecha}"

# from django.db import models

# # Create your models here.

# # class Reserva:
# #
# #     def __init__(self, nombre_de_usuario, destino):
# #         self.nombre_de_usuario = nombre_de_usuario
# #         self.destino = destino
# # 
# #     def __str__(self):
# #         return f"Esta es una reserva de {self.nombre_de_usuario} con destino a {self.destino}"


# class Reserva(models.Model):
#     nombre_de_usuario = models.CharField(max_length=50)
#     destino = models.CharField(max_length=50)

#     def __str__(self):
#         return f"Esta es una reserva de {self.nombre_de_usuario} con destino a {self.destino}"