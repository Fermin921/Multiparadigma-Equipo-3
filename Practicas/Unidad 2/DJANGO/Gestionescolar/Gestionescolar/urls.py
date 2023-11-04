"""
URL configuration for Gestionescolar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Escuela.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("inicio", index),
    # Clase
    path("ListadoClase", indexClase, name="ListadoClase"),
    path("nuevaclase", nuevaclase),
    path("detalleClase/<int:id>", Detalleclase),
    path("editarClase/<int:id>", editarclase),
    path("EliminarClase/<int:id>", Eliminarclase),
    # Calificacion
    path("ListadoCalificacion", indexCalificacion, name="ListadoCalificacion"),
    path("nuevaCalificacion", nuevaCalificacion),
    path("detalleCalificacion/<int:id>", DetalleCalificacion),
    path("editarCalificacion/<int:id>", editarCalificacion),
    path("EliminarCalificacion/<int:id>", EliminarCalificacion),
    # Asistencia
    path("ListadoAsistencias", indexAsistencia, name="ListadoAsistencias"),
    path("nuevaAsistencia", nuevaAsistencia),
    path("detalleAsistencia/<int:id>", DetalleAsistencia),
    path("editarAsistencia/<int:id>", editarAsistencia),
    path("EliminarAsistencia/<int:id>", EliminarAsistencia),
]
