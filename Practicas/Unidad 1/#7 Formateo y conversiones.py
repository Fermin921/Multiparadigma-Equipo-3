# Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir
# YYYY/MM/DD” la segunda “2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha
# del día de hoy en el formato seleccionado.
import datetime

fechaActual=datetime.date.today()

while True:
    TipoFecha = int(input("¿Como desea imprimir la fecha? \n 1.YYYY/MM/DD \n 2.MM/DD/YYYY \n "))
    if TipoFecha == 1:
        print(datetime.date.strftime(fechaActual,'%y/%m/%d'))
        break
    elif TipoFecha == 2:
        print(datetime.date.strftime(fechaActual,'%m/%d/%y'))
        break
    else:
        print("Ingresó una opción que no existe en el menú.")
