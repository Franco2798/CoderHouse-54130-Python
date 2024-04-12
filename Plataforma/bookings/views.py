from django.shortcuts import render
from django.http import HttpResponse

from .models import Reserva

# Create your views here.

def home_view(request):
    return render(request, "bookings/home.html")


def list_view(request):
    reservas = Reserva.objects.all()
    contexto_dict = {'todas_las_reservas': reservas}
    return render(request, "bookings/list.html", contexto_dict)


def search_view(request, nombre_de_usuario):
    reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
    contexto_dict = {"reservas": reservas_del_usuario}
    return render(request, "bookings/list.html", contexto_dict)


def detail_view(request, booking_id):
    reserva = Reserva.objects.get(id=booking_id)
    contexto_dict = {"reserva": reserva}
    return render(request, "bookings/detail.html", contexto_dict)

# from django.shortcuts import render
# from django.http import HttpResponse

# from .models import Reserva

# # Create your views here.

# def home_view(request):
#     return render(request, "bookings/home.html")

# """
# def list_view(request):
#     contexto_dict = {
#         'reservas': [
#             {"usuario": "Emiliano Martínez ", "destino": "venezuela"},
#             {"usuario": "Nicolas Otamendi ", "destino": "cuba"},
#             {"usuario": "Nahuel Molina ", "destino": "angola"},
#             {"usuario": "Gonzalo Montiel ", "destino": "marte"},
#             {"usuario": "Lisando Martinez ", "destino": "italia"},
#             {"usuario": "Angel di maria", "destino": "usa"},
#             {"usuario": "Julián Álvarez", "destino": "noruega"},
#         ]
#     }
#     return render(request, "list.html", contexto_dict)
# """

# def detail_view(request, booking_id):
#     reserva = Reserva.objects.get(id=booking_id)
#     contexto_dict = {"reserva": reserva}
#     return render(request, "bookings/detail.html", contexto_dict)

# def list_view(request):
#     reservas = Reserva.objects.all()
#     contexto_dict = {'reservas': reservas}
#     return render(request, "bookings/list.html", contexto_dict)

# def search_view(request, nombre_de_usuario):
#     reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
#     contexto_dict = {"reservas": reservas_del_usuario}
#     return render(request, "bookings/list.html", contexto_dict)


# """
# def create_view(request, nombre_de_usuario, destino):

#     # reserva = Reserva("", nombre_de_usuario, destino)
#     reserva = Reserva.objects.create(nombre_de_usuario=nombre_de_usuario, destino=destino)

#     return HttpResponse(f"resultado: {reserva}")

# """