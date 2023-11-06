from django.shortcuts import render
from gestorapp.models import *


# Create your views here.
def index(request):
    return render(request, "index.html")


def indexBebe(request):
    bebes = Bebe.objects.order_by("id")
    return render(request, "bebes/index.html", {"bebes": bebes})


def indexActividad(request):
    actividades = Actividad.objects.order_by("id")
    return render(request, "actividades/index.html", {"actividades": actividades})


def indexAsistencia(request):
    asistencias = Asistencia.objects.order_by("id")
    return render(request, "asistencias/index.html", {"asistencias": asistencias})


def indexEmpleado(request):
    empleados = Empleado.objects.order_by("id")
    return render(request, "empleados/index.html", {"empleados": empleados})


def indexPadre(request):
    padres = Padre.objects.order_by("id")
    return render(request, "padres/index.html", {"padres": padres})
