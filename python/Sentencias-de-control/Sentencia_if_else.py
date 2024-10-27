"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 23 - 10 -2024
Descripción: Programa que determina si un número ingresado por el usuario es par o impar utilizando la estructura de control if-else.
"""

"""
La sentencia if-else es una estructura de control fundamental que permite tomar decisiones en el código.
Dependiendo de si se cumple una determinada condición, el programa tomará un camino u otro.

Sintaxis:

if condición:
    # Código a ejecutar si la condición es verdadera.

else:
    # Código a ejecutar si la condición es falsa.

# Código que se ejecuta sin importar la condición.
"""

print("\tPrograma para verificar si un número es par o impar")
print()
# Solicita al usuario que ingrese un número y convierte el valor ingresado a un entero.
num = int(input("Ingrese un número: "))

# La estructura if verifica si el número es par, al verificar si el módulo del número ingresado dividido por 2 es igual a 0.
if num % 2 == 0:
    print(f"El número {num} es par")
else:
    # Si la condición no se cumple, el número es impar.
    print(f"El número es {num} impar")