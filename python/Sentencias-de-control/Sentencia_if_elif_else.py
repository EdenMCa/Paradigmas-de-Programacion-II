"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 23 - 10 -2024
Descripción: En este programa se muestra cómo se usa if-elif-else para organizar a personas de acuerdo a su edad
en distintos grupos de edad de una manera estructurada, garantizando que cada persona pertenezca a un único grupo.
"""

"""
La sentencia elif es una extensión del if-else y permite evaluar múltiples condiciones de forma secuencial. 
Es como tener varias opciones a elegir, ejecutándose el bloque de código correspondiente a la primera condición 
que sea verdadera.

Sintaxis:

if condicion_1:
    # Código a ejecutar si la condición_1 es verdadera.

elif condición_2:
    # Código a ejecutar si la condición_2 es verdadera.
  .
  .
  .
else:
    # Código que se ejecuta si todas las condiciones fueron falsas.
"""

print("\t Programa que determina grupos de edad")
print()
# Se le solicita al usuario que ingrese su edad y convierte el valor ingresado a un entero.
edad = int(input("Ingrese su edad: "))

# La estructura if evalúa si la edad ingresada es menor a 15.
if edad < 15:
    # Si la edad es menor que 15, se clasifica como "niños y adolescentes".
    print("Usted pertenece a niños y adolescentes")
# elif verifica si la edad está entre 15 y 24.
elif edad <= 24:
    # Si la edad está en este rango, se clasifica como "jóvenes".
    print("Usted pertenece a jóvenes")
# Otro bloque elif evalúa si la edad está entre 25 y 44.
elif edad <= 44:
    #Si esta condición se cumple, imprime el mensaje.
    print("Usted pertenece a adultos jóvenes")
# Verifica que las edades estén entre 45 y 60
elif edad <=60:
    print("Usted pertenece a adultos maduros")
# Si todas las condiciones anteriores son falsas y la edad es mayor a 60, se clasifica como "adultos mayores".
elif edad > 60:
    print("Usted pertenece a adultos mayores")
# A diferencia de una simple estructura if-else, elif permite manejar múltiples opciones sin necesidad de escribir
# múltiples if separados.
