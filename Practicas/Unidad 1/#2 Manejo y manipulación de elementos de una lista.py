# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen
# posiciones múltiplos de 2, y muestre por pantalla la lista resultante

Abecedario = [chr(i) for i in range(97, 123)]

for i in range(len(Abecedario) - 1, -1, -1):
    if (i % 2) == 0:
        del Abecedario[i-1]

print(Abecedario)
