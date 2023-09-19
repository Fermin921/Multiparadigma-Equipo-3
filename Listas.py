# Lista vacía
mi_lista = []

# Lista con elementos
mi_lista = [1, 2, 3, 4, 5]

# Para acceder al elemento en la posición 2
elemento = mi_lista[2]  # Esto devolverá 3

# Cambiar el valor del elemento en la posición 1
mi_lista[1] = 10

# Añadir un elemento al final de la lista
mi_lista.append(6)

# Extender la lista con otra lista
mi_lista.extend([7, 8, 9])

# Insertar un elemento en una posición específica
mi_lista.insert(2, 20)

# Eliminar el elemento en la posición 3
del mi_lista[3]

# Eliminar el último elemento de la lista
mi_lista.pop()

# Eliminar un elemento por su valor
mi_lista.remove(5)

# Eliminar todos los elementos de la lista
mi_lista.clear()

indice = mi_lista.index(4)  # Devuelve el índice del primer elemento igual a 4

# Verificar si existe un elemento en la lista
if 3 in mi_lista:
    print("El 3 está en la lista")

mi_lista.sort()  # Ordena la lista de forma ascendente
mi_lista.sort(reverse=True)  # Ordena la lista de forma descendente

# Sacar la longitud de la lista
longitud = len(mi_lista)

# Copias la lista
copia_lista = mi_lista.copy()
