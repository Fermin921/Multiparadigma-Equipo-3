# Crear un set con elementos
mi_set = {1, 2, 3, 4, 5}

# Crear un set vacío
set_vacio = set()

mi_set.add(6)
mi_set.update([7, 8, 9])  # Puedes agregar varios elementos a la vez

mi_set.remove(3)
# O puedes usar discard si no estás seguro de si el elemento está presente
mi_set.discard(10)

# Eliminar y retornar un elemento aleatorio
elemento_eliminado = mi_set.pop()

# Verificar si un objeto esta en el set
esta_en_el_set = 5 in mi_set

longitud = len(mi_set)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Unión de sets
union_set = set1.union(set2)

# Intersección de sets
interseccion_set = set1.intersection(set2)

# Diferencia de sets (elementos en set1 pero no en set2)
diferencia_set = set1.difference(set2)

# Diferencia simétrica (elementos que están en uno u otro, pero no en ambos)
diferencia_simetrica_set = set1.symmetric_difference(set2)

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Verificar si set1 es subconjunto de set2
es_subconjunto = set1.issubset(set2)

# Verificar si set2 es superconjunto de set1
es_superconjunto = set2.issuperset(set1)

# Vaciar un set
copia_set = mi_set.copy()

mi_set.clear()  # El set quedará vacío

for elemento in mi_set:
    print(elemento)
