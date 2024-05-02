from django.db import models
from django.utils import timezone

class Vuelo(models.Model):
    nombre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)
    capacidad = models.IntegerField()
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha = models.DateField(default=timezone.now)
    hora_salida = models.TimeField(default=timezone.now)
    hora_llegada = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} - {self.origen} - {self.destino} - {'Disponible' if self.disponible else 'No Disponible'}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.nombre} - {self.dni}"

class Reserva(models.Model):
    nombre_de_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuarios')
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE, related_name='vuelos')
    cantidad_de_pasajeros = models.IntegerField()
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_de_usuario.nombre} - {self.vuelo.nombre}"


