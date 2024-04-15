from django import forms

from .models import Reserva, Sala


class ReservaSearchForm(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=50, required=True, label="Ingresar nombre de usuario")


class ReservaCreateForm(forms.Form):
    pass


class SalaCreateForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nombre', 'disponible', 'capacidad', 'descripcion']
        # widgets = {
        #     'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describa la sala...'}),
        #     'capacidad': forms.NumberInput(attrs={'min': 1, 'placeholder': 'Capacidad máxima de personas'}),
        #     'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la sala'}),
        #     # 'disponible' does not need a custom widget for a simple checkbox.
        # }
        labels = {
            'nombre': 'Elegir un nombre para la Sala',
            'disponible': 'Disponible',
            'capacidad': 'Capacidad máxima',
            'descripcion': 'Descripción',
        }
