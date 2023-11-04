# Generated by Django 4.2.7 on 2023-11-03 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.PositiveIntegerField()),
                ('semestre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('materia', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estudiante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Escuela.estudiante')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Escuela.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.DecimalField(decimal_places=2, max_digits=5)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Escuela.clase')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Escuela.estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('asistencia_estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Escuela.estudiante')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Escuela.clase')),
            ],
        ),
    ]
