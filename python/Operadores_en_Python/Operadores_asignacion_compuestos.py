"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 18 - 10 - 2024
Descripción: Este programa utiliza operadores de asignación compuesta para realizar una serie de cálculos
sobre dos números ingresados por el usuario. A medida que se realizan las operaciones, las mismas
variables se utilizan, lo que actualiza sus valores después de cada operación.
"""

"""
Los operadores de asignación compuestos son una forma abreviada de realizar una operación aritmética y una asignación
en una sola línea de código. Combinan un operador aritmético (como suma, resta, multiplicación, división, etc.) 
con el operador de asignación (=).
"""

num1 = float(input("Ingrese el primer número: ")) # Se solicita al usuario que ingrese el primer número.
num2 = float(input("Ingrese el segundo número: ")) # Se solicita al usuario que ingrese el segundo número.

num1 += 4 # Suma 4 a num1
print(f"El resultado de sumar 4 a num1 es: {num1}")
#El valor de num1 se actualiza después de esta operación.
#Los valores se actualizan después de cada operación.
num2 -= 6 # Resta 6 a num2
print(f"El resultado de restar 6 a num2 es: {num2}")
#El valor de num2 se actualiza después de esta operación.

num1 *= 21 # Multiplica num1 por 21
print(f"El resultado de multiplicar num1 por 21 es: {num1}")

num2 /= 11 # Divide num2 entre 11
print(f"El resultado de dividir num2 entre 11 es: {num2}")

num1 %= 14 # Calcula el residuo de num1 dividido entre 14
print(f"El resultado de calcular el residuo de num1 dividido entre 14 es: {num1}")

num2 **= 2 # Eleva num2 al cuadrado
print(f"El resultado de elevar num2 al cuadrado es: {num2}")

num2 //= 3 # Realiza una división entera de num2 entre 3
print(num2)




