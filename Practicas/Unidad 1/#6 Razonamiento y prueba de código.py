# Escribir un programa que reciba un numero entre 0 y 20 e imprimir el numero en letra, no utilizar
# condicionales, máximo 5 líneas de código

numletras = [
    "cero",
    "uno",
    "dos",
    "tres",
    "cuatro",
    "cinco",
    "seis",
    "siete",
    "ocho",
    "nueve",
    "diez",
    "once",
    "doce",
    "trece",
    "catorce",
    "quince",
    "dieciséis",
    "diecisiete",
    "dieciocho",
    "diecinueve",
    "veinte",
]

numero = int(input("Ingrese un número entre 0 y 20: "))
print(numletras[numero])
