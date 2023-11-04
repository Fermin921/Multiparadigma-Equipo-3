from django.shortcuts import render, redirect, get_object_or_404
from Escuela.models import *
from Escuela.forms import *


# Vistas
# Agregar una nueva persona
def nuevaclase(request):
    if request.method == "POST":
        formaClase = ClaseForm(request.POST)
        if formaClase.is_valid():
            formaClase.save()
            return redirect("ListadoClase")
    else:
        formaClase = ClaseForm()
    return render(request, "Clase/AgregarClase.html", {"formaClase": formaClase})


# Metodo para editar persona
def editarclase(request, id):
    clase = get_object_or_404(Clase, pk=id)
    if request.method == "POST":
        formaClase = ClaseForm(request.POST, instance=clase)
        if formaClase.is_valid():
            formaClase.save()
            return redirect("ListadoClase")
    else:
        formaClase = ClaseForm(instance=clase)
    return render(request, "Clase/editarClase.html", {"formaClase": formaClase})


# EliminarClase
def Eliminarclase(request, id):
    clase = get_object_or_404(Clase, pk=id)
    if clase:
        clase.delete()
    return redirect("ListadoClase")


# ConsultarClase
def Detalleclase(request, id):
    clase = get_object_or_404(Clase, pk=id)
    return render(request, "Clase/detalleClase.html", {"clase": clase})


# Create your views here.
def index(request):
    return render(request, "index.html")


def indexClase(request):
    clases = Clase.objects.order_by("id")

    return render(request, "Clase/indexClase.html", {"clases": clases})


# Calificacion
def indexCalificacion(request):
    calificaciones = Calificacion.objects.order_by("id")

    return render(
        request,
        "Calificaciones/indexCalificacion.html",
        {"calificaciones": calificaciones},
    )


# Agregar una nueva calificacion
def nuevaCalificacion(request):
    if request.method == "POST":
        formaCalificacion = CalificacionForm(request.POST)
        if formaCalificacion.is_valid():
            formaCalificacion.save()
            return redirect("ListadoCalificacion")
    else:
        formaCalificacion = CalificacionForm()
    return render(
        request,
        "Calificaciones/AgregarCalificacion.html",
        {"formaCalificacion": formaCalificacion},
    )


# Metodo para editar calificacion
def editarCalificacion(request, id):
    calificacion = get_object_or_404(Calificacion, pk=id)
    if request.method == "POST":
        formaCalificacion = CalificacionForm(request.POST, instance=calificacion)
        if formaCalificacion.is_valid():
            formaCalificacion.save()
            return redirect("ListadoCalificacion")
    else:
        formaCalificacion = CalificacionForm(instance=calificacion)
    return render(
        request,
        "Calificaciones/EditarCalificacion.html",
        {"formaCalificacion": formaCalificacion},
    )


# Eliminar Calificacion
def EliminarCalificacion(request, id):
    calificacion = get_object_or_404(Calificacion, pk=id)
    if calificacion:
        calificacion.delete()
    return redirect("ListadoCalificacion")


# Consultar calificaciones
def DetalleCalificacion(request, id):
    calificacion = get_object_or_404(Calificacion, pk=id)
    return render(
        request,
        "Calificaciones/DetalleCalificacion.html",
        {"Calificacion": calificacion},
    )


# Asistencias
def indexAsistencia(request):
    asistencias = Asistencia.objects.order_by("id")

    return render(
        request,
        "Asistencias/indexAsistencia.html",
        {"asistencias": asistencias},
    )


# Agregar una nueva asistencia
def nuevaAsistencia(request):
    if request.method == "POST":
        formaAsistencia = AsistenciaForm(request.POST)
        if formaAsistencia.is_valid():
            formaAsistencia.save()
            return redirect("ListadoAsistencias")
    else:
        formaAsistencia = AsistenciaForm()
    return render(
        request,
        "Asistencias/AgregarAsistencia.html",
        {"formaAsistencia": formaAsistencia},
    )


# Metodo para editar asistencias
def editarAsistencia(request, id):
    asistencia = get_object_or_404(Asistencia, pk=id)
    if request.method == "POST":
        formaAsistencia = AsistenciaForm(request.POST, instance=asistencia)
        if formaAsistencia.is_valid():
            formaAsistencia.save()
            return redirect("ListadoAsistencias")
    else:
        formaAsistencia = AsistenciaForm(instance=asistencia)
    return render(
        request,
        "Asistencias/EditarAsistencia.html",
        {"formaAsistencia": formaAsistencia},
    )


# Eliminar asistencia
def EliminarAsistencia(request, id):
    asistencia = get_object_or_404(Asistencia, pk=id)
    if asistencia:
        asistencia.delete()
    return redirect("ListadoAsistencias")


# Consultar calificaciones
def DetalleAsistencia(request, id):
    asistencia = get_object_or_404(Asistencia, pk=id)
    return render(
        request,
        "Asistencias/DetalleAsistencia.html",
        {"asistencia": asistencia},
    )
