# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen
# posiciones múltiplos de 2, y muestre por pantalla la lista resultante

ListaParaEliminar = []
Abecedario = [chr(i) for i in range(97, 123)]
for i in range(len(Abecedario)):
    if (i % 2) == 0:
        ListaParaEliminar.append(Abecedario[i-1])

for f in ListaParaEliminar:
    Abecedario.remove(f)

print(Abecedario)
