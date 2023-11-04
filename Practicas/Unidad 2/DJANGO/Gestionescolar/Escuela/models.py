from django.db import models


# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    semestre = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    materia = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(
        Estudiante, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.estudiante:
            Clase.objects.filter(estudiante=self.estudiante).exclude(pk=self.pk).update(
                estudiante=None
            )


class Calificacion(models.Model):
    curso = models.ForeignKey(Clase, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Calificación de {self.estudiante.nombre} en {self.curso.nombre}"


class Asistencia(models.Model):
    curso = models.ForeignKey(Clase, on_delete=models.CASCADE)
    fecha = models.DateField()
    asistencia_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"Asistencia de {self.asistencia_estudiante.nombre} en {self.curso.nombre}"
        )


class Materia(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
