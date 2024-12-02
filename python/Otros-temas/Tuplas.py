"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 13 - 11 -2024
Descripción: Este programa utiliza una tupla para almacenar un conjunto de calificaciones de un parcial.
"""
"""
Una tupla es una colección ordenada e inmutable de elementos. Esto significa que:
 - Ordenada: Los elementos se almacenan en un orden específico, y cada elemento tiene un índice asociado.
 - Inmutable: Una vez creada, no se puede agregar, eliminar o cambiar elementos dentro de una tupla.
 - Heterogénea: Una tupla puede contener elementos de diferentes tipos de datos.

Sintaxis para crear una lista:
Se encierra los elementos entre paréntesis () y se separan por comas. 
Nota: el uso de los paréntesis es opcional.
"""

# Definición de una tupla con calificaciones de un parcial
calificaciones_parcial1 = (9.6,6.3,6.0,8.7,5.0)

# Asignamos datos de la tupla en variables individuales
poo, bd, redes, ara, ing_s = calificaciones_parcial1
print(calificaciones_parcial1)

# Imprimimos cada calificación en la tupla separada por comas
for calificacion in calificaciones_parcial1:
    print(calificacion, end = ", ")
"""
# El siguiente código está comentado porque 'remove' no se puede usar con tuplas (es inmutable)
calificaciones_parcial1.remove(6.3)
print(calificaciones_parcial1)
"""

# Cálculo del promedio de las calificaciones
print()
"""
El programa calcula el promedio de las calificaciones utilizando la función sum() para obtener
la suma de los elementos de la tupla y len() para contar cuántos elementos hay, luego imprime el resultado.
"""
promedio_parcial1 = sum(calificaciones_parcial1)/len(calificaciones_parcial1)
print(f"Promedio: {promedio_parcial1}")
