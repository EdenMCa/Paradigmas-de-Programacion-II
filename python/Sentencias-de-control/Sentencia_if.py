"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 23 - 10 -2024
Descripción: Este programa utiliza una estructura de control if para verificar si el usuario es mayor de edad.
"""

"""
La sentencia de control if es una estructura de control fundamental que permite ejecutar diferentes bloques de código
 dependiendo de si una condición se cumple o no.

Sintaxis:

if condición:
    # Código a ejecutar si la condición es verdadera. Notar que hay que dejar un espacio de tabulador.

# Código que se continúa ejecutando. Notar que ya no hay espacio y está a la misma altura que el if.
"""

# Ejemplo en donde se imprime un mensaje si el usuario tiene la mayoría de edad.
print("\t Programa para verificar si eres mayor de edad")
print()
# Se solicita al usuario que ingrese su edad y se convierte el valor ingresado a un entero.
edad = int(input("Ingresa tu edad: "))

# La estructura if evalúa si la edad ingresada es mayor o igual a 18.
if edad >= 18:
    # Si la condición es verdadera, imprime que el usuario es mayor de edad.
    print("Eres mayor de edad")
#Si la condición no se cumple, se aborta el programa.
