"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 14 - 11 -2024
Descripción: Ejemplos de uso de los conjuntos
"""
"""
Un conjunto en Python es una colección desordenada de elementos únicos. Esto significa que:
    -> No hay elementos duplicados: Cada elemento aparece solo una vez en el conjunto.
    -> No hay orden: Los elementos no están ordenados de ninguna manera específica.
    -> Son mutables: Se puede modificar después de crearlo, agregando o eliminando elementos.

Sintaxis para crear un conjunto:
Se encierra los elementos entre llaves {} y se separan por comas. 
Nota: Lo anterior aplica, excepto para crear un conjunto vacío.
"""
# Conjunto vacío
conjunto1 = set()
conjunto2 = {10,5,24,11,8,7,21,9}
print(conjunto2)
conjunto1.add(80)
conjunto1.add(111)
conjunto1.add(10)
conjunto1.add(5)
conjunto1.add(24)
print()
print(conjunto1)
conjunto1.add(80)
print()
print(conjunto1)
conjunto1.remove(111)
print(conjunto1)
#El remove funciona SOLO si el elemento EXISTE.
conjunto1.discard(111)# No genera error si no está el número que queremos eliminar
conjunto1.remove(10)
print(conjunto1)

#Unión del conjunto1 con el conjunto2
conjunto_union = conjunto1 | conjunto2
print(conjunto_union)

conjunto_interseccion = conjunto1 & conjunto2
print(conjunto_interseccion)# Muestra los números repetidos.

resta_conjuntos = conjunto2 - conjunto1
print(resta_conjuntos)

alumnos_lista = ["Albert", "Kevin", "Elton", "Diana", "Eden", "Amelia", "Sergio"]
alumnos_lista.append("Elton")
alumnos_conjunto = set(alumnos_lista) # Transforma una lista a un conjunto
print(alumnos_conjunto)
print()
print(alumnos_lista)

nombre = input("Ingresa un nombre: ")
"""
alumnos_lista.append(nombre)
alumnos_conjunto.add(nombre)
print(alumnos_lista)
print(alumnos_conjunto)
"""
nombre = nombre.strip().lower()
if nombre in alumnos_conjunto:
    print(f"Se encuentra en alumnos conjunto")
else:
    print("Se añadió al conjunto")
alumnos_conjunto.add(nombre)