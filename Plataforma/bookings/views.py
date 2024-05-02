from django.shortcuts import render, redirect

from .forms import ReservaCreateForm, ReservaSearchForm, VueloCreateForm, UsuarioViajeroSearchForm
from .models import Reserva, Vuelo, Usuario

from django.contrib.auth.decorators import login_required


def create_with_form_view(request):
    if request.method == "GET":
        contexto = {"PAPPO": ReservaCreateForm()}
        return render(request, "bookings/form-create.html", contexto)
    elif request.method == "POST":
        form = ReservaCreateForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data["nombre_de_usuario"]
            vuelo = form.cleaned_data["vuelo"]
            cantidad_de_pasajeros = form.cleaned_data["cantidad_de_pasajeros"]
            descripcion = form.cleaned_data["descripcion"]
            nueva_reserva = Reserva(
                nombre_de_usuario=nombre_de_usuario,
                vuelo=vuelo,
                cantidad_de_pasajeros=cantidad_de_pasajeros,
                descripcion=descripcion,
            )
            nueva_reserva.save()
            return detail_view(request, nueva_reserva.id)


@login_required
def create_vuelo_with_form_view(request):
    if request.method == "GET":
        contexto = {"LUISMIGUEL": VueloCreateForm()}
        return render(request, "bookings/form-create-vuelo.html", contexto)
    elif request.method == "POST":
        form = VueloCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            disponible = form.cleaned_data["disponible"]
            capacidad = form.cleaned_data["capacidad"]
            origen = form.cleaned_data["origen"]
            destino = form.cleaned_data["destino"]
            fecha = form.cleaned_data["fecha"]
            hora_salida = form.cleaned_data["hora_salida"]
            hora_llegada = form.cleaned_data["hora_llegada"]
            nuevo_vuelo = Vuelo(
                nombre=nombre,
                disponible=disponible,
                capacidad=capacidad,
                origen=origen,
                destino=destino,
                fecha=fecha,
                hora_salida=hora_salida,
                hora_llegada=hora_llegada,
            )
            nuevo_vuelo.save()
            return detail_vuelo_view(request, nuevo_vuelo.id)


def home_view(request):
    return render(request, "bookings/home.html")


@login_required
def list_view(request):
    reservas = Reserva.objects.all()
    contexto_dict = {"todas_las_reservas": reservas}
    return render(request, "bookings/list.html", contexto_dict)


def search_view(request, nombre_de_usuario):
    reservas_del_usuario = Reserva.objects.filter(
        nombre_de_usuario=nombre_de_usuario
    ).all()
    contexto_dict = {"reservas": reservas_del_usuario}
    return render(request, "bookings/list.html", contexto_dict)


def search_with_form_view(request):
    if request.method == "GET":
        # devuelvo el formulario vacio
        contexto = {"CERATI": ReservaSearchForm()}
        return render(request, "bookings/form-search.html", contexto)
    elif request.method == "POST":
        form = ReservaSearchForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data["nombre_de_usuario"]
            reservas_del_usuario = Reserva.objects.filter(nombre_de_usuario__nombre__icontains=nombre_de_usuario)
            contexto = {"todas_las_reservas": reservas_del_usuario}
            return render(request, "bookings/list.html", contexto)


def detail_view(request, booking_id):
    reserva = Reserva.objects.get(id=booking_id)
    contexto_dict = {"reserva": reserva}
    return render(request, "bookings/detail.html", contexto_dict)


def detail_vuelo_view(request, vuelo_id):
    vuelo = Vuelo.objects.get(id=vuelo_id)
    contexto_dict = {"vuelo": vuelo}
    return render(request, "bookings/detail-vuelo.html", contexto_dict)


# -----------------------------------------------------------------------------
# CLASE 22
# -----------------------------------------------------------------------------

# CRUD
from django.http import HttpResponse


@login_required
def vuelo_list_view(request):
    todos_los_vuelos = Vuelo.objects.all()
    contexto = {"SANTIAGOMOTORIZADO": todos_los_vuelos}
    return render(request, "bookings/vuelos/list.html", contexto)


def vuelo_delete_view(request, vuelo_id):
    vuelo_a_borrar = Vuelo.objects.filter(id=vuelo_id).first()
    vuelo_a_borrar.delete()
    return redirect("vuelo-list")

def reserva_delete_view(request, reserva_id):
    reserva_a_borrar = Reserva.objects.filter(id=reserva_id).first()
    reserva_a_borrar.delete()
    return redirect("bookings-list")


def vuelo_update_view(request, vuelo_id):
    vuelo_a_editar = Vuelo.objects.filter(id=vuelo_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "nombre": vuelo_a_editar.nombre,
            "disponible": vuelo_a_editar.disponible,
            "capacidad": vuelo_a_editar.capacidad,
            "origen": vuelo_a_editar.origen,
            "destino": vuelo_a_editar.destino,
            "fecha": vuelo_a_editar.fecha,
            "hora_salida": vuelo_a_editar.hora_salida,
            "hora_llegada": vuelo_a_editar.hora_llegada,
        }
        formulario = VueloCreateForm(initial=valores_iniciales)
        contexto = {"ENRIQUE": formulario, "OBJETO": vuelo_a_editar}
        return render(request, "bookings/vuelos/form_update.html", contexto)
    elif request.method == "POST":
        form = VueloCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            disponible = form.cleaned_data["disponible"]
            capacidad = form.cleaned_data["capacidad"]
            origen = form.cleaned_data["origen"]
            destino = form.cleaned_data["destino"]
            fecha = form.cleaned_data["fecha"]
            hora_salida = form.cleaned_data["hora_salida"]
            hora_llegada = form.cleaned_data["hora_llegada"]
            vuelo_a_editar.nombre = nombre
            vuelo_a_editar.disponible = disponible
            vuelo_a_editar.capacidad = capacidad
            vuelo_a_editar.origen = origen
            vuelo_a_editar.destino = destino
            vuelo_a_editar.fecha = fecha
            vuelo_a_editar.hora_salida = hora_salida
            vuelo_a_editar.hora_llegada = hora_llegada
            vuelo_a_editar.save()
            return redirect("vuelo-detail", vuelo_a_editar.id)
        

def reserva_update_view(request, reserva_id):
    reserva_a_editar = Reserva.objects.filter(id=reserva_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "nombre_de_usuario": reserva_a_editar.nombre_de_usuario,
            "vuelo": reserva_a_editar.vuelo,
            "cantidad_de_pasajeros": reserva_a_editar.cantidad_de_pasajeros,
            "descripcion": reserva_a_editar.descripcion,
        }
        formulario = ReservaCreateForm(initial=valores_iniciales)
        contexto = {"MOLLO": formulario, "GUITARRA": reserva_a_editar}
        return render(request, "bookings/form-update.html", contexto)
    elif request.method == "POST":
        form = ReservaCreateForm(request.POST)
        if form.is_valid():
            nombre_de_usuario = form.cleaned_data["nombre_de_usuario"]
            vuelo = form.cleaned_data["vuelo"]
            cantidad_de_pasajeros = form.cleaned_data["cantidad_de_pasajeros"]
            descripcion = form.cleaned_data["descripcion"]
            reserva_a_editar.nombre_de_usuario = nombre_de_usuario
            reserva_a_editar.vuelo = vuelo
            reserva_a_editar.cantidad_de_pasajeros = cantidad_de_pasajeros
            reserva_a_editar.descripcion = descripcion
            reserva_a_editar.save()
            return redirect("detail-view", reserva_a_editar.id)
        



from .forms import VueloSearchForm


@login_required
def search_vuelo_view(request):
    if request.method == "GET":
        # devuelvo el formulario vacio
        contexto = {"ARJONA": VueloSearchForm()}
        return render(request, "bookings/vuelos/form_search.html", contexto)
    elif request.method == "POST":
        form = VueloSearchForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            vuelos = Vuelo.objects.filter(nombre__icontains=nombre)
            contexto = {"SANTIAGOMOTORIZADO": vuelos}
            return render(request, "bookings/vuelos/list.html", contexto)
    
    return render(request, "bookings/vuelos/form_search.html", contexto)


# Vistas basadas en clases "VBC"

from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib.auth.mixins import LoginRequiredMixin


# class SalaListView(LoginRequiredMixin, ListView):
#     model = Sala
#     template_name = "bookings/vbc/sala_list.html"
#     context_object_name = "ADRIANDARGELOS"


# class SalaDetailView(LoginRequiredMixin, DetailView):
#     model = Sala
#     template_name = "bookings/vbc/sala_detail.html"
#     context_object_name = "GUSTAVOCERATI"


# class SalaCreateView(LoginRequiredMixin, CreateView):
#     model = Sala
#     template_name = "bookings/vbc/sala_form.html"
#     fields = ["nombre", "disponible", "capacidad", "descripcion"]
#     success_url = reverse_lazy("vbc_sala_list")


# class SalaUpdateView(LoginRequiredMixin, UpdateView):
#     model = Sala
#     template_name = "bookings/vbc/sala_form.html"
#     fields = ["nombre", "disponible", "capacidad", "descripcion"]
#     context_object_name = "sala"
#     success_url = reverse_lazy("vbc_sala_list")


# class SalaDeleteView(LoginRequiredMixin, DeleteView):
#     model = Sala
#     template_name = "bookings/vbc/sala_confirm_delete.html"
#     success_url = reverse_lazy("vbc_sala_list")


# -----------------------------------------------------------------------------
# CLASE 23
# -----------------------------------------------------------------------------
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


def user_login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect("home")

    return render(request, "bookings/login.html", {"MICHAELSTIPE": form})


from django.contrib.auth.forms import UserCreationForm


def user_creation_view(request):
    if request.method == "GET":
        form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    return render(request, "bookings/crear_usuario.html", {"form": form})


from django.contrib.auth import logout


def user_logout_view(request):
    logout(request)
    return redirect("login")


# -----------------------------------------------------------------------------
# CLASE 24
# -----------------------------------------------------------------------------


from django.contrib.auth.models import User
from .forms import UserEditForm

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'bookings/user_edit_form.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    

from .forms import UsuarioViajeroCreateForm, UsuarioViajeroSearchForm

@login_required
def create_usuario_viajero(request):
    if request.method == "GET":
        contexto = {"INDIOSOLARI": UsuarioViajeroCreateForm()}
        return render(request, "bookings/usuarios/crear-usuario-viajero.html", contexto)
    elif request.method == "POST":
        form = UsuarioViajeroCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            edad = form.cleaned_data["edad"]
            nacionalidad = form.cleaned_data["nacionalidad"]
            dni = form.cleaned_data["dni"]
            nuevo_usuario_viajero = Usuario(
                nombre=nombre,
                edad=edad,
                nacionalidad=nacionalidad,
                dni=dni,
            )
            nuevo_usuario_viajero.save()
            return detail_usuario_viajero(request, nuevo_usuario_viajero.id)
        
def detail_usuario_viajero(request, usuario_viajero_id):
    usuario_viajero = Usuario.objects.get(id=usuario_viajero_id)
    contexto_dict = {"usuario_viajero": usuario_viajero}
    return render(request, "bookings/usuarios/ver-usuario-viajero.html", contexto_dict)

def list_usuarios(request):
    usuarios = Usuario.objects.all()
    contexto_dict = {"todos_los_usuarios": usuarios}
    return render(request, "bookings/usuarios/list-usuarios.html", contexto_dict)

def editar_usuario_viajero(request, usuario_viajero_id):
    usuario_a_editar = Usuario.objects.filter(id=usuario_viajero_id).first()
    if request.method == "GET":
        valores_iniciales = {
            "nombre": usuario_a_editar.nombre,
            "edad": usuario_a_editar.edad,
            "nacionalidad": usuario_a_editar.nacionalidad,
            "dni": usuario_a_editar.dni,
        }
        formulario = UsuarioViajeroCreateForm(initial=valores_iniciales)
        contexto = {"SKAY": formulario, "POLY": usuario_a_editar}
        return render(request, "bookings/usuarios/editar-usuario-viajero.html", contexto)
    elif request.method == "POST":
        form = UsuarioViajeroCreateForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            edad = form.cleaned_data["edad"]
            nacionalidad = form.cleaned_data["nacionalidad"]
            dni = form.cleaned_data["dni"]
            usuario_a_editar.nombre = nombre
            usuario_a_editar.edad = edad
            usuario_a_editar.nacionalidad = nacionalidad
            usuario_a_editar.dni = dni
            usuario_a_editar.save()
            return redirect("ver-usuario-viajero", usuario_a_editar.id)
        

def eliminar_usuario_viajero(request, usuario_viajero_id):
    usuario_a_borrar = Usuario.objects.filter(id=usuario_viajero_id).first()
    usuario_a_borrar.delete()
    return redirect("list-usuario-viajero")


def buscar_usuario_viajero(request):
    if request.method == "GET":
        # devuelvo el formulario vacio
        contexto = {"CHIZZO": UsuarioViajeroSearchForm()}
        return render(request, "bookings/usuarios/buscar-usuario-viajero.html", contexto)
    elif request.method == "POST":
        form = UsuarioViajeroSearchForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            usuarios_viajeros = Usuario.objects.filter(nombre__icontains=nombre)
            contexto = {"todos_los_usuarios": usuarios_viajeros}
            return render(request, "bookings/usuarios/list-usuarios.html", contexto)
    
    return render(request, "bookings/vuelos/buscar-usuario-viajero.html", contexto)
        
    
    
    

