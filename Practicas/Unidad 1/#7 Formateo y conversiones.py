# Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir
# YYYY/MM/DD” la segunda “2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha
# del día de hoy en el formato seleccionado.
import datetime


def ImprimirFecha1():
    FechaActual = datetime.datetime.today()
    print(f"{FechaActual.year}/{FechaActual.month}/{FechaActual.day}")


def ImprimirFecha2():
    FechaActual = datetime.datetime.today()
    print(f"{FechaActual.month}/{FechaActual.day}/{FechaActual.year}")


while True:
    TipoFecha = int(
        input("¿Como desea imprimir la fecha? \n 1.YYYY/MM/DD \n 2.MM/DD/YYYY \n ")
    )
    if TipoFecha == 1:
        print(ImprimirFecha1())
        break
    elif TipoFecha == 2:
        print(ImprimirFecha2())
        break
    else:
        print("Ingreso un valor erroneo del menu")
