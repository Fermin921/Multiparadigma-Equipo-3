from django.forms import ModelForm, EmailInput
from Escuela.models import *


class ClaseForm(ModelForm):
    class Meta:
        model = Clase
        fields = "__all__"


class CalificacionForm(ModelForm):
    class Meta:
        model = Calificacion
        fields = ["curso", "estudiante", "calificacion"]


class AsistenciaForm(ModelForm):
    class Meta:
        model = Asistencia
        fields = "__all__"
