from django.forms import *
from gestorapp.models import *


class BebeForm(ModelForm):
    class Meta:
        model = Bebe
        fields = "__all__"
        widgets = {
            "fecha_nacimiento": DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "style": "max-width: 100px;",
                }
            ),
            "alergias": Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Alergias (opcional)",
                }
            ),
        }


class PadreForm(ModelForm):
    class Meta:
        model = Padre
        fields = "__all__"
        widgets = {
            "correo_electronico": EmailInput(
                attrs={
                    "type": "email",
                    "class": "form-control",
                    "style": "max-width:100 px",
                    "placeholder": "Correo",
                }
            )
        }


class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"


class ActividadForm(ModelForm):
    class Meta:
        model = Actividad
        fields = "__all__"


class AsistenciaForm(ModelForm):
    class Meta:
        model = Asistencia
        fields = "__all__"
