from django import forms

from .models import Reserva, Vuelo, Usuario


class ReservaSearchForm(forms.Form): 
    nombre_de_usuario = forms.CharField(
        max_length=50, required=True, label="Ingresar nombre de usuario"
    )


class VueloSearchForm(forms.Form):
    nombre = forms.CharField(
        max_length=50, required=True, label="Ingresar nombre del vuelo"
    )


class VueloCreateForm(forms.ModelForm):
    class Meta:
        model = Vuelo
        fields = ["nombre", "disponible", "capacidad", "origen", "destino", "fecha", "hora_salida", "hora_llegada"]
        labels = {
            "nombre": "Elegir el nombre del vuelo",
            "disponible": "Disponible",
            "capacidad": "Capacidad máxima",
            "origen": "Ciudad de Origen",
            "destino": "Ciudad de Destino",
            "fecha": "Fecha del vuelo",
            "hora_salida": "Horario de salida",
            "hora_llegada": "Horario de llegada",
        }
        widgets = {
            "fecha": forms.DateInput(
                attrs={"type": "date"}
            ),  # Use HTML5 date picker for the 'fecha' field
            "hora_salida": forms.TimeInput(
                attrs={"type": "time"}
            ),  # Use HTML5 time input for 'hora_inicio'
            "hora_llegada": forms.TimeInput(
                attrs={"type": "time"}
            ),  # Use HTML5 time input for 'hora_fin'
            
        }


# class ReservaSearchForm(forms.Form):
#     nombre_de_usuario = forms.CharField(max_length=50, required=False, label="Nombre de Usuario")
#     sala = forms.ModelChoiceField(queryset=Sala.objects.all(), required=False, label="Sala")

#     def __init__(self, *args, **kwargs):
#         super(ReservaSearchForm, self).__init__(*args, **kwargs)
#         self.fields['sala'].queryset = Sala.objects.filter(disponible=True) if self.data.get('disponible') else Sala.objects.all()


class ReservaCreateForm(forms.ModelForm):
    class Meta:
        model = Reserva
        # Specifying which fields should appear in the form, including 'sala'
        fields = [
            "nombre_de_usuario",
            "vuelo",
            "cantidad_de_pasajeros",
            "descripcion",
        ]

        widgets = {
            "descripcion": forms.Textarea(
                attrs={"rows": 3}
            ),  # Provide a larger text area for 'descripcion'
        }
        

    def __init__(self, *args, **kwargs):
        super(ReservaCreateForm, self).__init__(*args, **kwargs)
        # Optionally, you can further customize the 'sala' field here, for example:
        self.fields["vuelo"].queryset = Vuelo.objects.filter(
            disponible=True
        )  # Limit choices to available rooms
        self.fields["vuelo"].label = "Vuelo"  # Customize the field label
        # Any other field customizations can be done here


# -----------------------------------------------------------------------------
# CLASE 24
# -----------------------------------------------------------------------------

from django.contrib.auth.models import User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UsuarioViajeroCreateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        # Specifying which fields should appear in the form, including 'sala'
        fields = [
            "nombre",
            "edad",
            "nacionalidad",
            "dni",
        ]


class UsuarioViajeroSearchForm(forms.Form):
    nombre = forms.CharField(
        max_length=50, required=True, label="Ingresar nombre del usuario viajero"
    )