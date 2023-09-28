# Escribir un programa que reciba un numero entre 0 y 20 e imprimir el numero en letra, no utilizar
# condicionales, máximo 5 líneas de código

numletra = {0: 'cero', 1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro', 5: 'cinco', 6: 'seis', 7: 'siete', 8: 'ocho', 9: 'nueve', 10: 'diez', 11: 'once', 12: 'doce', 13: 'trece', 14: 'catorce', 15: 'quince', 16: 'dieciséis', 17: 'diecisiete', 18: 'dieciocho', 19: 'diecinueve', 20: 'veinte'}

numero = int(input("Ingrese un número entre 0 y 20: "))
print(numletra.get(numero, "Número no válido"))