from django.shortcuts import render, redirect, get_object_or_404
from gestorapp.models import Bebe, Padre, Empleado, Actividad, Asistencia
from gestorapp.form import (
    BebeForm,
    PadreForm,
    EmpleadoForm,
    ActividadForm,
    AsistenciaForm,
)


# Agregar un nuevo bebé
def agregarBebe(request):
    if request.method == "POST":
        formabebe = BebeForm(request.POST)
        if formabebe.is_valid():
            formabebe.save()
            return redirect("ListadoBebes")
    else:
        formabebe = BebeForm()
    return render(request, "bebes/agregar.html", {"formabebe": formabebe})


# Método para editar un bebé
def editarBebe(request, id):
    bebe = get_object_or_404(Bebe, pk=id)
    if request.method == "POST":
        formabebe = BebeForm(request.POST, instance=bebe)
        if formabebe.is_valid():
            formabebe.save()
            return redirect("ListadoBebes")
    else:
        formabebe = BebeForm(instance=bebe)
    return render(request, "bebes/editar.html", {"formabebe": formabebe})


# Eliminar un bebé
def eliminarBebe(request, id):
    bebe = get_object_or_404(Bebe, pk=id)
    if bebe:
        bebe.delete()
    return redirect("ListadoBebes")


# Consultar detalles de un bebé
def detalleBebe(request, id):
    bebe = get_object_or_404(Bebe, pk=id)
    return render(request, "bebes/detalle.html", {"bebe": bebe})


# Agregar un nuevo padre
def agregarPadre(request):
    if request.method == "POST":
        formapadre = PadreForm(request.POST)
        if formapadre.is_valid():
            formapadre.save()
            return redirect("ListadoPadres")
    else:
        formapadre = PadreForm()
    return render(request, "padres/agregar.html", {"formapadre": formapadre})


# Método para editar un padre
def editarPadre(request, id):
    padre = get_object_or_404(Padre, pk=id)
    if request.method == "POST":
        formapadre = PadreForm(request.POST, instance=padre)
        if formapadre.is_valid():
            formapadre.save()
            return redirect("ListadoPadres")
    else:
        formapadre = PadreForm(instance=padre)
    return render(request, "padres/editar.html", {"formapadre": formapadre})


# Eliminar un padre
def eliminarPadre(request, id):
    padre = get_object_or_404(Padre, pk=id)
    if padre:
        padre.delete()
    return redirect("ListadoPadres")


# Consultar detalles de un padre
def detallePadre(request, id):
    padre = get_object_or_404(Padre, pk=id)
    return render(request, "padres/detalle.html", {"padre": padre})


# Agregar un nuevo empleado
def agregarEmpleado(request):
    if request.method == "POST":
        formaempleado = EmpleadoForm(request.POST)
        if formaempleado.is_valid():
            formaempleado.save()
            return redirect("ListadoEmpleados")
    else:
        formaempleado = EmpleadoForm()
    return render(request, "empleados/agregar.html", {"formaempleado": formaempleado})


# Método para editar un empleado
def editarEmpleado(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    if request.method == "POST":
        formaempleado = EmpleadoForm(request.POST, instance=empleado)
        if formaempleado.is_valid():
            formaempleado.save()
            return redirect("ListadoEmpleados")
    else:
        formaempleado = EmpleadoForm(instance=empleado)
    return render(request, "empleados/editar.html", {"formaempleado": formaempleado})


# Eliminar un empleado
def eliminarEmpleado(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    if empleado:
        empleado.delete()
    return redirect("ListadoEmpleados")


# Consultar detalles de un empleado
def detalleEmpleado(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    return render(request, "empleados/detalle.html", {"empleado": empleado})


# Agregar una nueva actividad
def agregarActividad(request):
    if request.method == "POST":
        formaactividad = ActividadForm(request.POST)
        if formaactividad.is_valid():
            formaactividad.save()
            return redirect("ListadoActividades")
    else:
        formaactividad = ActividadForm()
    return render(
        request, "actividades/agregar.html", {"formaactividad": formaactividad}
    )


def detalleActividad(request, id):
    actividad = get_object_or_404(Actividad, pk=id)
    return render(request, "actividades/detalle.html", {"actividad": actividad})


# Método para editar una actividad
def editarActividad(request, id):
    actividad = get_object_or_404(Actividad, pk=id)
    if request.method == "POST":
        formaactividad = ActividadForm(request.POST, instance=actividad)
        if formaactividad.is_valid():
            formaactividad.save()
            return redirect("ListadoActividades")
    else:
        formaactividad = ActividadForm(instance=actividad)
    return render(
        request, "actividades/editar.html", {"formaactividad": formaactividad}
    )


# Eliminar una actividad
def eliminarActividad(request, id):
    actividad = get_object_or_404(Actividad, pk=id)
    if actividad:
        actividad.delete()
    return redirect("ListadoActividades")


# Consultar detalles de una asistencia
def detalleAsistencia(request, id):
    asistencia = get_object_or_404(Asistencia, pk=id)
    return render(request, "asistencias/detalle.html", {"asistencia": asistencia})


# Agregar una nueva asistencia
def agregarAsistencia(request):
    if request.method == "POST":
        formaAsistencia = AsistenciaForm(request.POST)
        if formaAsistencia.is_valid():
            formaAsistencia.save()
            return redirect("ListadoAsistencias")
    else:
        formaAsistencia = AsistenciaForm()
    return render(
        request, "asistencias/agregar.html", {"formaAsistencia": formaAsistencia}
    )


# Método para editar una asistencia
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
        request, "asistencias/editar.html", {"formaAsistencia": formaAsistencia}
    )


# Eliminar una asistencia
def eliminarAsistencia(request, id):
    asistencia = get_object_or_404(Asistencia, pk=id)
    if asistencia:
        asistencia.delete()
    return redirect("ListadoAsistencias")
