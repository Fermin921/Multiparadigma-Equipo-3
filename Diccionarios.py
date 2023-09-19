# Crear un diccionario vacío
mi_diccionario = {}

# Crear un diccionario con elementos
mi_diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Acceder a un valor por su clave
print(mi_diccionario["nombre"])  # Output: Juan

# También puedes usar el método get() para acceder a un valor
print(mi_diccionario.get("edad"))  # Output: 30

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Modificar el valor de una clave
mi_diccionario["edad"] = 31

print(mi_diccionario)  # Output: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid'}

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Agregar una nueva clave-valor
mi_diccionario["profesion"] = "Ingeniero"

print(
    mi_diccionario
)  # Output: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid', 'profesion': 'Ingeniero'}

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Eliminar una clave y su valor
del mi_diccionario["ciudad"]

print(mi_diccionario)  # Output: {'nombre': 'Juan', 'edad': 30}

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Verificar si una clave existe
print("nombre" in mi_diccionario)  # Output: True
print("profesion" in mi_diccionario)  # Output: False

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Iterar sobre las claves
for clave in mi_diccionario:
    print(clave, mi_diccionario[clave])

# Otra forma de iterar sobre claves y valores
for clave, valor in mi_diccionario.items():
    print(clave, valor)

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Copiar un diccionario
copia_diccionario = mi_diccionario.copy()

# También puedes usar el constructor dict() para hacer una copia
copia_diccionario = dict(mi_diccionario)

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Limpiar un diccionario (eliminar todos los elementos)
mi_diccionario.clear()

print(mi_diccionario)  # Output: {}
