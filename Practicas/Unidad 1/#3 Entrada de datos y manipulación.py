# Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de
# manera inversa letra por letra intercalando una letra minuscula a una mayuscula ejemplo Luis : L u I s

Nombre = input("Favor de ingresar su nombre completo: ")
Nombre2 = ""
for i in range(len(Nombre)):
    if ((i + 1) % 2) == 0:
        Nombre2 += Nombre[i].lower()
    else:
        Nombre2 += Nombre[i].upper()

print(Nombre2)
