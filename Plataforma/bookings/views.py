from django.shortcuts import render
from .models import Reserva, Sala
from .forms import ReservaSearchForm, ReservaCreateForm, SalaCreateForm

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


def detail_sala_view(request, sala_id):
    sala = Sala.objects.get(id=sala_id)
    contexto_dict = {"sala": sala}
    return render(request, "bookings/detail-sala.html", contexto_dict)



def search_with_form_view(request):
    if request.method == "GET":
        form = ReservaSearchForm()
        return render(request, "bookings/form-search.html", context={"search_form": form})
    elif request.method == "POST":
        form = ReservaSearchForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']
        reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario=nombre_de_usuario).all()
        contexto_dict = {"todas_las_reservas": reservas_del_usuario}
        return render(request, "bookings/list.html", contexto_dict)
    

def create_with_form_view(request):
    contexto = {"create_form": ReservaCreateForm()}
    return render(request, "bookings/form-create.html", contexto)


def create_sala_with_form_view(request):
    if request.method == "GET":
        contexto = {"create_form": SalaCreateForm()}
        return render(request, "bookings/form-create.html", contexto)
    elif request.method == "POST":
        form = SalaCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            disponible = form.cleaned_data['disponible']
            capacidad = form.cleaned_data['capacidad']
            descripcion = form.cleaned_data['descripcion']
            nueva_sala = Sala(nombre=nombre, disponible=disponible, descripcion=descripcion, capacidad=capacidad)
            nueva_sala.save()
            return detail_sala_view(nueva_sala.id)




    
    
    

