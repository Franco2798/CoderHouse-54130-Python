from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    return HttpResponse("<h3>Bienvenidos a la aplicación de Reservas 'Bookings'</h3>")

def list_view(request):
    contexto_dict = {
        'reservas': [
            {"usuario": "Emiliano Martínez ", "destino": "venezuela"},
            {"usuario": "Nicolas Otamendi ", "destino": "cuba"},
            {"usuario": "Nahuel Molina ", "destino": "angola"},
            {"usuario": "Gonzalo Montiel ", "destino": "marte"},
            {"usuario": "Lisando Martinez ", "destino": "italia"},
            {"usuario": "Angel di maria", "destino": "usa"},
            {"usuario": "Julián Álvarez", "destino": "noruega"},
        ]
    }
    return render(request, "list.html", contexto_dict)

def search_view(request, nombre_de_usuario):
    print("-" * 90)
    print("-" * 90)
    print(request.method)
    print(nombre_de_usuario)
    print("-" * 90)
    print("-" * 90)
    return HttpResponse(f"<h3>Has pedido buscar las reservas de: {nombre_de_usuario}</h3>")
