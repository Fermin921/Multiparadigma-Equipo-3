#crear una matriz (lista de listas) de n x n donde n >= 2 y n <= 10 se creara una funcion que llene
#la matriz de manera automatica, despues crear una funcion donde en forma de caracol empezando por 
#(0,0) se copien los numeros de la matriz llenada automaticamente pero en orden de menor a mayor.
def GenerarMatriz(n):
    if n < 2 or n > 10:
        raise ValueError("n debe estar en el rango [2, 10]")
    
    matriz = [[0] * n for _ in range(n)]
    numero = 1
    
    for capa in range((n + 1) // 2):
        for i in range(capa, n - capa):
            matriz[capa][i] = numero
            numero += 1
        for i in range(capa + 1, n - capa):
            matriz[i][n - capa - 1] = numero
            numero += 1
        for i in range(capa + 1, n - capa):
            matriz[n - capa - 1][n - i - 1] = numero
            numero += 1
        for i in range(capa + 1, n - capa - 1):
            matriz[n - i - 1][capa] = numero
            numero += 1
    
    return matriz

def GenerarCaracol(matriz):
    resultado = []
    while matriz:
        resultado += matriz.pop(0)
        if matriz and matriz[0]:
            for fila in matriz:
                resultado.append(fila.pop())
        if matriz:
            resultado += matriz.pop()[::-1]
        if matriz and matriz[0]:
            for fila in matriz[::-1]:
                resultado.append(fila.pop(0))
    return resultado

while True:
    try:
        n = int(input("Ingrese el valor de n (n >= 2 y n <= 10):  "))
        if n < 0 or n < 2 or n > 10:
            print("Debes ingresar numeros enteros positivos y en el rango valido.")
        else:
            break
    except ValueError:
        print("Debes ingresar un numero entero.")

matriz = GenerarMatriz(n)
print("Matriz generada:")
for fila in matriz:
    print(fila)

