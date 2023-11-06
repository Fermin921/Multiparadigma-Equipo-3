"""
URL configuration for Examen project.

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
from webapp.views import *
from gestorapp.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index),
    path("ListadoBebes", indexBebe, name="ListadoBebes"),
    path("agregarBebe", agregarBebe),
    path("editarBebe/<int:id>", editarBebe),
    path("eliminarBebe/<int:id>", eliminarBebe),
    path("detalleBebe/<int:id>", detalleBebe),
    path("ListadoActividades", indexActividad, name="ListadoActividades"),
    path("agregarActividad", agregarActividad, name="agregarActividad"),
    path("editarActividad/<int:id>", editarActividad, name="editarActividad"),
    path("eliminarActividad/<int:id>", eliminarActividad, name="eliminarActividad"),
    path("detalleActividad/<int:id>", detalleActividad, name="detalleActividad"),
    path("ListadoAsistencias", indexAsistencia, name="ListadoAsistencias"),
    path("agregarAsistencia", agregarAsistencia, name="agregarAsistencia"),
    path("editarAsistencia/<int:id>", editarAsistencia, name="editarAsistencia"),
    path("eliminarAsistencia/<int:id>", eliminarAsistencia, name="eliminarAsistencia"),
    path("detalleAsistencia/<int:id>", detalleAsistencia, name="detalleAsistencia"),
    path("ListadoEmpleados", indexEmpleado, name="ListadoEmpleados"),
    path("agregarEmpleado", agregarEmpleado, name="agregarEmpleado"),
    path("editarEmpleado/<int:id>", editarEmpleado, name="editarEmpleado"),
    path("eliminarEmpleado/<int:id>", eliminarEmpleado, name="eliminarEmpleado"),
    path("detalleEmpleado/<int:id>", detalleEmpleado, name="detalleEmpleado"),
    path("ListadoPadres", indexPadre, name="ListadoPadres"),
    path("agregarPadre", agregarPadre, name="agregarPadre"),
    path("editarPadre/<int:id>", editarPadre, name="editarPadre"),
    path("eliminarPadre/<int:id>", eliminarPadre, name="eliminarPadre"),
    path("detallePadre/<int:id>", detallePadre, name="detallePadre"),
]
