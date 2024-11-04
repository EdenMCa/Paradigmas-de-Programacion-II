"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 29 - 10 -2024
Descripción: Este programa permite al usuario ingresar un número final y, a partir de ese número, se genera una secuencia
de resultados basados en la divisibilidad de los números enteros desde 1 hasta el número ingresado por el usuario.
"""

print("\t *** Licenciatura en Informática ***")
print()

# Solicitamos al usuario que ingrese el número final de la cuenta y lo almacenamos como entero en la variable numero_final.
numero_final = int(input("Ingrese el número final de la cuenta: "))

i = 1 # Inicializamos el contador i en 1 para comenzar la secuencia de números a evaluar hasta numero_final
while i <= numero_final: # Inicia el bucle que se ejecuta mientras i sea menor o igual a numero_final
    if i % 3 == 0 and i % 5 == 0:# Verifica si i es divisible por 3 y 5
        print("Licenciatura en informática", end = "\n") # Si i es divisible por ambos, imprime el mensaje.

    elif i % 3 == 0: # Verifica si i es divisible solo por 3
        print("Licenciatura", end = ", ") # Si i es divisible solo por 3, imprime "Licenciatura" seguido de una coma.

    elif i % 5 == 0: # Verifica si i es divisible solo por 5
        print("Informática", end = ", ") # Si i es divisible solo por 5, imprime "Informática" seguido de una coma.

    else: # Si i no es divisible por 3 ni por 5, imprime el número
        print(i, end = ", ")

    i += 1 # Incrementa el contador i en 1 para pasar al siguiente número.

