"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 30 - 10 -2024
Descripción: Este programa es un juego iterativo en el que el jugador debe adivinar un número aleatorio generado
por el sistema dentro del rango 1 al 100. El jugador cuenta con 5 intentos y con pistas.
"""
# Importa la función randint del módulo random para generar números aleatorios
from random import randint

print("\t *** Juego del adivinador ***")
# Genera un número aleatorio entre 1 y 100 que el jugador deberá adivinar
num_adivinar = randint(1, 100)
# Inicializa el contador de intentos en 1
intentos = 1
# Inicia un bucle que permite al jugador hasta 5 intentos para adivinar el número
while intentos < 6:
    # Solicita al jugador que ingrese un número y lo convierte a entero
    num_jugador = int(input(f"Número de intento: {intentos}. Ingresa un número (1-100): "))

    # Verifica si el número ingresado por el jugador es igual al número a adivinar
    if num_jugador == num_adivinar:
        # Si adivina correctamente, muestra un mensaje de felicitación y el número de intentos
        print(f"¡Felicidades!, adivinaste en {intentos} intentos.")
        # Sale del bucle si se adivina el número
        break
    # Verifica si el número ingresado es mayor que el número a adivinar
    elif num_jugador > num_adivinar:
        # Informa al jugador que el número a adivinar es menor
        print("El número a adivinar es menor.")
    # Verifica si el número ingresado es menor que el número a adivinar
    elif num_jugador < num_adivinar:
        # Informa al jugador que el número a adivinar es mayor
        print("El número a adivinar es mayor")
    # Incrementa el contador de intentos
    intentos += 1

    print()

# Después de 5 intentos, verifica si el jugador no ha adivinado el número
if intentos > 5:
    # Muestra un mensaje de pérdida y revela el número a adivinar
    print(f"Perdiste. El número era: {num_adivinar}")




