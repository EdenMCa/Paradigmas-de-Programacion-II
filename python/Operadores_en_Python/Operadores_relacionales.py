"""
Nombre: Mendoza Casarrubia Rosendo Edén
Fecha: 18 - 10 - 2024
Descripción: Este programa compara dos valores ingresados por el usuario mediante operadores relacionales.
Los resultados indican si el primer valor cumple con cada condición relacional en comparación con el segundo.
"""

print("Ingrese dos valores")

num1 = float(input("Ingrese el primer valor: "))
# Se solicita el primer valor y lo convierte a tipo float, permitiendo así el uso de números decimales
num2 = float(input("Ingrese el segundo valor: "))
# Solicita el segundo valor y lo convierte también a tipo float

mayor = num1 > num2
# Determina si num1 es mayor que num2 y almacena el resultado booleano en la variable 'mayor'
print(f"¿El número {num1:.2f} es mayor que el {num2:.2f}? {mayor}") #Se imprime el mensaje en este formato para una mayor claridad.
# El .2f nos indica que el número contará con 2 decimales.

menor = num1 < num2 # Determina si num1 es menor que num2 y almacena el resultado en la variable 'menor'
print(f"¿El número {num1:.2f} es menor que el {num2:.2f}? {menor}")

mayor_igual = num1 >= num2 # Determina si num1 es mayor o igual a num2 y almacena el resultado en la variable 'mayor_igual'
print(f"¿El número {num1:.2f} es mayor igual que el {num2:.2f}? {mayor_igual}")

menor_igual = num1 <= num2 # Determina si num1 es menor o igual a num2 y almacena el resultado en la variable 'menor_igual'
print(f"¿El número {num1:.2f} es menor igual que el {num2:.2f}? {menor_igual}")

# Comprueba si num1 es igual a num2, devolviendo un valor booleano en la impresión.
print(f"¿El número {num1:.2f} es igual igual que el {num2:.2f}? {num1 == num2}")

# Comprueba si num1 es diferente de num2.
print(f"¿El número {num1:.2f} es diferente que el {num2:.2f}? {num1 != num2}")
