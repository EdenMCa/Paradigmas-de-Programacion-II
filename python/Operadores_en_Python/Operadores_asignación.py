"""
Nombre:
Fecha: 17 - 10 - 2024
Descripción:
"""
print("Aignacióm múltiple")
num1, num2 = 7, 10

print(num1)
print(num2)

num3, cad, num4 = 11, "Hola", 9
print(" ")
print(num3)
print(cad)
print(num4)

suma, resta = num1 + num2, num3 - num4
print(" ")
print(suma)
print(resta)

print("Asignació encadenada")
num5 = num6 = num7 = 12
print(" ")
print(num5)
print(num6)
print(num7)

print(" ")
print("Intercambio de variables")
num8 = int(input("Ingrese un número: "))
num9 = int(input("Ingrese un número: "))

print(num8, num9)

num9, num8 = num8, num9
print(num8, num9)

print(" ")
print("Multiples variables de entrada")
num10, num11 = int(input("Ingrese un número: ")), int(input("Ingrese otro número: "))
print(num10, num11)