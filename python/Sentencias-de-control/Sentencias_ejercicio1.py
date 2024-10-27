"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 23 - 10 -2024
Descripción: Este programa está diseñado para comparar dos números decimales ingresados por el usuario
y determinar cuál de ellos es mayor, menor o si son iguales.
"""
print("\t Programa que determina cuál de los números es menor")
print()
# Se solicita al usuario ingresar el primer número decimal.
# La función input() recibe la entrada como cadena, y float() convierte la cadena a un valor decimal para realizar operaciones numéricas.
num1 = float(input("Ingresa un número con decimal: "))
# Solicita al usuario ingresar el segundo número decimal y convierte la entrada a float.
num2 = float(input("Ingresa otro número con decimal: "))

# En esta primera condición se evalúa si el primer número es mayor que el segundo.
if num1 > num2:
    # Si la condición es verdadera (num1 es mayor que num2), imprime un mensaje indicando que el primer número es mayor.
    print(f"El número {num1} es mayor al número {num2}")
# Verifica si el primer número es menor que el segundo, utilizamos "elif" para evaluar esta condición.
elif num1 < num2:
    # Si la condición es verdadera (num1 es menor que num2), imprime un mensaje indicando que el primer número es menor.
    print(f"El número {num1} es menor al número {num2}")
# La última condición se ejecuta solo si las dos condiciones anteriores son falsas, dando a entender que ambos números son iguales.
else:
    print(f"El número {num1} es igual al número {num2}")

