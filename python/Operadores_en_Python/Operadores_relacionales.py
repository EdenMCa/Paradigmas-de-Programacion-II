"""
Nombre: Mendoza Casarrubia Rosendo Edén
Fecha: 18 - 10 - 2024
"""

print("Ingrese dos valores")
num1 = float(input("Ingrese el primer valor: "))
num2 = float(input("Ingrese el segundo valor: "))

mayor = num1 > num2
print(f"¿El número {num1:.2f} es mayor que el {num2:.2f}? {mayor}")

menor = num1 < num2
print(f"¿El número {num1:.2f} es menor que el {num2:.2f}? {menor}")

mayor_igual = num1 >= num2
print(f"¿El número {num1:.2f} es mayor igual que el {num2:.2f}? {mayor_igual}")

menor_igual = num1 <= num2
print(f"¿El número {num1:.2f} es menor igual que el {num2:.2f}? {menor_igual}")

menor_igual = num1 <= num2
print(f"¿El número {num1:.2f} es menor igual que el {num2:.2f}? {menor_igual}")

print(f"¿El número {num1:.2f} es igual igual que el {num2:.2f}? {num1 == num2}")

print(f"¿El número {num1:.2f} es diferente que el {num2:.2f}? {num1 != num2}")
