# #Recorriendo por filas
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for fila in matriz:
#     for elemento in fila:
#         print(elemento, end=" ")
#     print()
# Va a imprimir
# 1 2 3
# 4 5 6
# 7 8 9

# #Recorriendo por indices
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # Recorriendo por índices
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j], end=" ")
#     print()

# Utilizando enumerate
# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # Utilizando enumerate
# for i, fila in enumerate(matriz):
#     for j, elemento in enumerate(fila):
#         print(f"matriz[{i}][{j}] = {elemento}")

# Va a imprimir lo siguiente:
# matriz[0][0] = 1
# matriz[0][1] = 2
# matriz[0][2] = 3
# matriz[1][0] = 4
# matriz[1][1] = 5
# matriz[1][2] = 6
# matriz[2][0] = 7
# matriz[2][1] = 8
# matriz[2][2] = 9

# Usando listas anidadas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Usando bibliotecas como NumPy (recomendado para operaciones matriciales avanzadas)
import numpy as np

matriz_numpy = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Para acceder al elemento en la fila 1, columna 2
elemento = matriz[1][2]  # Esto devolverá 6

# Recorriendo por filas y columnas
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()

num_filas = len(matriz)
num_columnas = len(matriz[0])


def sumar_matrices(matriz1, matriz2):
    resultado = [
        [matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))]
        for i in range(len(matriz1))
    ]
    return resultado


def multiplicar_escalar(matriz, escalar):
    resultado = [[elemento * escalar for elemento in fila] for fila in matriz]
    return resultado


def matriz_traspuesta(matriz):
    traspuesta = [
        [matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))
    ]
    return traspuesta


def multiplicar_matrices(matriz1, matriz2):
    resultado = [
        [
            sum(matriz1[i][k] * matriz2[k][j] for k in range(len(matriz2)))
            for j in range(len(matriz2[0]))
        ]
        for i in range(len(matriz1))
    ]
    return resultado


def es_simetrica(matriz):
    return matriz == matriz_traspuesta(matriz)


def diagonal_principal(matriz):
    return [matriz[i][i] for i in range(len(matriz))]
