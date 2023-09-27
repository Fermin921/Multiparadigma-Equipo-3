# Escribir una función que reciba n parámetros de llave valor e imprima la información en formato
# “{valor}”: “{llave}”


def Imprimirdiccionario(**kwargs):
    for key, parametro in kwargs.items():
        print(f'"{parametro}": "{key}"')


datos = {}
while True:
    Carrera = input("Favor de ingresar el nombre su carrera: ")
    Semestre = int(input("Ingrese el semestre que esta cursando: "))
    Nombre = input("Ingrese su nombre completo: ")
    NumControl = int(input("Ingrese su numero de control: "))
    datos["Carrera"] = Carrera
    datos["Semestre"] = Semestre
    datos["Nombre"] = Nombre
    datos["NumControl"] = NumControl

    Pregunta = int(input("¿Quiere seguir agregando informacion? (1.Si 2.NO): "))
    if Pregunta != 1:
        break

Imprimirdiccionario(**datos)
