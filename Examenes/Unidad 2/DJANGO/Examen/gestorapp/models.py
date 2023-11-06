from django.db import models


class Bebe(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    alergias = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Padre(models.Model):
    nombre = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Asistencia(models.Model):
    bebe = models.ForeignKey(Bebe, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f"Asistencia de {self.bebe} a {self.actividad} el {self.fecha}"
