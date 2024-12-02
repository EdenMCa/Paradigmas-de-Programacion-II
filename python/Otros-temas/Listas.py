"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 11 - 11 -2024
Descripción: Este programa nos demuestra las operaciones básicas para trabajar con listas.
"""
"""
Una lista en Python es una colección ordenada y mutable de elementos. Esto significa que:
 - Ordenada: Los elementos se almacenan en un orden específico, y cada elemento tiene un índice asociado.
 - Mutable: Puedes modificar una lista después de su creación, agregando, eliminando o cambiando elementos.
 - Heterogénea: Una lista puede contener elementos de diferentes tipos de datos (enteros, cadenas, flotantes, incluso otras listas).

Sintaxis para crear una lista:
Se encierra los elementos entre corchetes [] y sepáralos por comas.

Listas:
    -> Ordenada
    -> Mutable
    -> Heterogeneo
"""

# alumnos = [] Listas vacías
print("\t* * * L I S T A S * * *")
print()
# Se crea una lista llamada 'alumnos' con dos elementos iniciales: "Amelia" y "Albert"
alumnos = ["Amelia", "Albert"]
print(alumnos) # Mostramos la lista
print()

# Se añade al alumno "Kevin" al final de la lista usando el metodo append()
alumnos.append("Kevin") # Añade un elemento al final de la lista
print(alumnos) # Mostramos la lista después de añadir el elemento.
print()

# Se añade a la alumna "Diana" al final de la lista
alumnos.append("Diana")
print(alumnos) # Mostramos la lista después de añadir el elemento.
print()

# Se añade al alumno "Elton" en el índice 3 de la lista usando insert()
alumnos.insert(3, "Elton")# Añade un elemento en un índice específico
print(alumnos)
print()
alumnos.insert(4, "Magdiel")
print(alumnos)
print()

# Se añade al alumno "Eden" al final de la lista
alumnos.append("Eden")
print(alumnos)
print()
alumnos.append("Sergio")
print(alumnos)
print()

# Se añade al alumno "Magdiel" en el índice 7 de la lista
alumnos.insert(7, "Magdiel")
print(alumnos)
print()
alumnos.insert(9, "Magdiel")
print(alumnos)
print()

# remove() elimina la primera aparición de un elemento específico.
alumnos.remove("Magdiel")
# Elimina un elemento de la lista especificando el valor del elemento como argumento.
# Si hay duplicados, solo elimina la primera aparición. Si el elemento no está en la lista, devuelve un error de valor.
print(alumnos)
print()

# Elimina un elemento de la lista especificando su índice. Por ejemplo, para eliminar el primer elemento,
# se especifica el índice 0, y para eliminar el último elemento, se especifica el índice -1.
alumnos.pop(6)
print(alumnos)
print()

"""
alumnos.pop(-1)
print(alumnos) # Para eliminar el último elemento, se especifica el índice -1
print()
"""

# Se elimina el elemento en el índice 7 usando del
# del elimina un elemento en una posición específica por índice sin devolver el valor eliminado
del alumnos[7]
print(alumnos)

"""
Funciones comunes
    -> Len()
    -> Sort()
    -> Sort(reverse = True)    
"""
