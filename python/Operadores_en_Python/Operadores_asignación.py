"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 17 - 10 - 2024
Descripción: Este programa muestra ejemplos de asignación múltiple, asignación encadenada, intercambio de variables y múltiples variables de entrada.
"""
print("Asignación múltiple")
num1, num2 = 7, 10 # Asigna valores a num1 y num2 simultáneamente.

# Imprime los valores de num1 y num2 para verificar la asignación
print(num1) # Muestra el valor de num1
print(num2) # Muestra el valor de num2

# Asignación múltiple con diferentes tipos de datos en una sola línea.
num3, cad, num4 = 11, "Hola", 9
print(" ") # Inserta una línea en blanco para mejorar la presentación.
# Imprime los valores de num3, cad (una cadena de texto), y num4, mostrando la versatilidad de la asignación múltiple
print(num3)
print(cad)
print(num4)

# Se realiza operaciones matemáticas en una sola línea, asignando los resultados a dos variables
suma, resta = num1 + num2, num3 - num4
print(" ")
# Imprime los resultados, podemos ver cómo los valores pueden ser manipulados directamente durante la asignación múltiple.
print(suma)
print(resta)

print("Asignación encadenada") # Asigna el mismo valor a varias variables
# Es útil cuando se necesita inicializar múltiples variables con el mismo valor
num5 = num6 = num7 = 12
print(" ")
# Imprime cada variable para confirmar que todas han recibido el valor 12.
print(num5)
print(num6)
print(num7)

print(" ")
print("Intercambio de variables")
# Solicita dos números al usuario y convierte cada entrada a entero
num8 = int(input("Ingrese un número: "))
num9 = int(input("Ingrese un número: "))

print(num8, num9) # Muestra los valores originales antes del intercambio para comparar los resultados posteriores


num9, num8 = num8, num9 # Intercambio de valores en una línea sin variable temporal.
print(num8, num9)  # Los valores se han intercambiado, el valor original de num8 ahora está en num9 y viceversa.
# Si a num8 le ingresamos 10 ahora 10 estará en num9

print(" ")
print("Multiples variables de entrada")
# Solicita dos entradas del usuario en una línea, convirtiéndolas a enteros y asignándolas a num10 y num11.
# Útil para ahorrar líneas de código.
num10, num11 = int(input("Ingrese un número: ")), int(input("Ingrese otro número: "))
print(num10, num11) # Muestra los valores de num10 y num11.