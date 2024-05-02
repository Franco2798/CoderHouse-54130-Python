from django.urls import path

from .views import (
    home_view,
    detail_view,
    list_view,
    search_view,
    search_with_form_view,
    create_with_form_view,
    create_vuelo_with_form_view,
    detail_vuelo_view,
    # -----------------------------------------------------------------------------
    # CLASE 22
    # -----------------------------------------------------------------------------
    # CRUD
    vuelo_list_view,
    vuelo_delete_view,
    vuelo_update_view,
    search_vuelo_view,
    # VBC
    # SalaListView,
    # SalaDetailView,
    # SalaDeleteView,
    # SalaUpdateView,
    # SalaCreateView,
    # -----------------------------------------------------------------------------
    # CLASE 23
    # -----------------------------------------------------------------------------
    user_login_view,
    user_creation_view,
    user_logout_view,
    # -----------------------------------------------------------------------------
    # CLASE 23
    # -----------------------------------------------------------------------------
    UserUpdateView,

    create_usuario_viajero,
    detail_usuario_viajero,
    list_usuarios,
    editar_usuario_viajero,
    eliminar_usuario_viajero,
    buscar_usuario_viajero,

    reserva_delete_view,
    reserva_update_view,
)

urlpatterns = [
    path("", home_view, name="home"),
    path("detail/<booking_id>", detail_view, name="detail-view"),
    path("list/", list_view, name="bookings-list"),
    path("buscar/<nombre_de_usuario>", search_view),
    # -----------------------------------------------------------------------------
    # CLASE 21
    # -----------------------------------------------------------------------------
    path("buscar-con-formulario/", search_with_form_view, name="zzz"),
    path("crear-reserva-con-formulario/", create_with_form_view, name="yyy"),
    path("vuelo/create/", create_vuelo_with_form_view, name="vuelo-create"),
    path("vuelo/detail/<vuelo_id>", detail_vuelo_view, name="vuelo-detail"),
    # -----------------------------------------------------------------------------
    # CLASE 22
    # -----------------------------------------------------------------------------
    # CRUD
    path("vuelo/list/", vuelo_list_view, name="vuelo-list"),
    path("vuelo/delete/<vuelo_id>", vuelo_delete_view, name="vuelo-delete"),
    path("vuelo/update/<vuelo_id>", vuelo_update_view, name="vuelo-update"),
    path("vuelo/buscar/", search_vuelo_view, name="vuelo-search"),
    # Vistas basadas en clases "VBC"
    # path("sala/vbc/list", SalaListView.as_view(), name="vbc_sala_list"),
    # path("sala/vbc/create/", SalaCreateView.as_view(), name="vbc_sala_create"),
    # path("sala/vbc/<int:pk>/detail", SalaDetailView.as_view(), name="vbc_sala_detail"),
    # path("sala/vbc/<int:pk>/update/", SalaUpdateView.as_view(), name="vbc_sala_update"),
    # path("sala/vbc/<int:pk>/delete/", SalaDeleteView.as_view(), name="vbc_sala_delete"),
    # -----------------------------------------------------------------------------
    # CLASE 23
    # -----------------------------------------------------------------------------
    path("crear-usuario/", user_creation_view, name="crear-usuario"),
    path("login/", user_login_view, name="login"),
    path("logout/", user_logout_view, name="logout"),
    # -----------------------------------------------------------------------------
    # CLASE 23
    # -----------------------------------------------------------------------------
    path('editar-perfil/', UserUpdateView.as_view(), name='editar-perfil'),
    #------------------#
    path("crear-usuario-viajero/", create_usuario_viajero, name="crear-usuario-viajero"),
    path("ver-usuario-viajero/<usuario_viajero_id>", detail_usuario_viajero, name="ver-usuario-viajero"),
    path("list-usuarios/", list_usuarios, name="list-usuario-viajero"),
    path("editar-usuario-viajero/<usuario_viajero_id>", editar_usuario_viajero, name="editar-usuario-viajero"),
    path("eliminar-usuario-viajero/<usuario_viajero_id>", eliminar_usuario_viajero, name="eliminar-usuario-viajero"),
    path("buscar-usuario-viajero/", buscar_usuario_viajero, name="buscar-usuario-viajero"),
    #------------------#
    path("reserva/delete/<reserva_id>", reserva_delete_view, name="reserva-delete"),
    path("reserva/update/<reserva_id>", reserva_update_view, name="reserva-update"),
]
