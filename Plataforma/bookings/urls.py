from django.urls import path

from .views import (
    home_view, 
    detail_view,
    detail_sala_view, 
    list_view, 
    search_view, 
    search_with_form_view, 
    create_with_form_view,
    create_sala_with_form_view,
    )


urlpatterns = [
    path("", home_view),
    path("detail/<booking_id>", detail_view),
    path("detail-sala/<sala_id>", detail_sala_view),
    path("list/", list_view, name="bookings-list"),
    path("buscar/<nombre_de_usuario>", search_view),
    path("buscar-con-formulario/", search_with_form_view, name="zzz"),
    path("crear-reserva-con-formulario/", create_with_form_view, name="yyy"),
    path("crear-sala-con-formulario/", create_sala_with_form_view, name="crear-sala-con-form"),
]
