# Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de
# manera inversa letra por letra intercalando una letra minuscula a una mayuscula ejemplo Luis : L u I s

NombreCompleto = input("Favor de ingresar su nombre completo: ")
NombreIntercalado = ""
for i in range(len(NombreCompleto)):
    if ((i + 1) % 2) == 0:
        NombreIntercalado += NombreCompleto[i].lower()
    else:
        NombreIntercalado += NombreCompleto[i].upper()

NombreInvertido = ''.join(reversed(NombreIntercalado))
print(NombreInvertido)
