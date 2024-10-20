"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 19 - 10 - 2024
Descripción: Este programa es una calculadora básica que solicita al usuario ingresar dos números decimales.
Realiza las siguientes operaciones aritméticas (suma, resta, multiplicación y división) con los
números ingresados y muestra los resultados en pantalla. El programa usa la función input() para obtener
la entrada del usuario y float() para realizar el cast a decimal.
"""

print("\t CALCULADORA BÁSICA") # Se imprime el título "CALCULADORA BÁSICA" con un tabulador ("\t") al inicio.
print() # Imprimimos una línea en blanco, para mejorar la presentación.
print("A continuación ingrese dos números decimales") # Se solicita al usuario que introduzca dos números decimales.
num1 = float(input("Ingrese el primer número: "))
# Se le pide al usuario que ingrese el primer número decimal.
# 'input()' obtiene el valor ingresado como cadena (string),
# con el 'float()' antes del 'input()' convertimos la cadena en un número decimal (tipo float).
num2 = float(input("Ingrese el segundo número diferente a cero: ")) # Sucede lo mismo que en la línea anterior, pero
# con una especificación, el número debe ser diferente a cero.

suma = num1 + num2 # Se realiza la operación de suma entre los dos números introducidos y se almacena en la variable 'suma'.
resta = num1 - num2 # Se realiza la operación de resta entre 'num1' y 'num2', y el resultado se almacena en 'resta'.
multiplicacion = num1 * num2 # Se realiza la operación de multiplicación entre los dos números y el resultado se almacena en 'multiplicacion'.
division = num1 / num2 # Se realiza la operación de división entre 'num1' y 'num2', y el resultado se almacena en 'division'.

# Utiliza la letra "f" antes de las comillas para indicar que la cadena será formateada.
# Esto significa que puedes incluir variables y expresiones dentro de las llaves {}
# y su valor será insertado en el texto final.
print (f"El resultado de la suma de {num1} + {num2} es: {suma}") # Se imprime el resultado de la suma usando una f-string para incluir los valores de 'num1', 'num2', y 'suma'.
print( f"EL resultado de la resta de {num1} - {num2} es: {resta}") # Se imprime el resultado de la resta de forma similar, utilizando los valores almacenados.
print(f"El resultado de la multiplicación de {num1} * {num2} es: {multiplicacion}") # Se imprime el resultado de la multiplicación.
print(f"El resultado de la división de {num1} / {num2} es: {division}") # Se imprime el resultado de la división.
