"""
Nombre: Rosendo Eden Mendoza Casarrubia
Fecha: 18 - 01 - 2025
Descripción: Este programa es un juego de adivinanza, en el que el jugador deberá adivinar un número generado aleatoriamento.
Después de cada juego, el historial de la partida se guarda en un archivo de texto (historial_adivinador.txt). Esto incluye la fecha del juego,
el número de intentos realizados, los intentos específicos del jugador, si ganó o no, y el número correcto en caso de que no haya adivinado.
"""
"""
Gestión de errores: Se incluye manejo de excepciones (try-except) para evitar que el programa se
detenga por entradas no válidas o problemas al escribir en el archivo.
"""
from random import randint # Importamos randint para generar un número aleatorio entre 1 y 100.
from datetime import datetime # Importamos datetime para registrar la fecha y hora.

# Función que guarda el historial del juego en un archivo.
def guardar_historial(intentos_realizados, intentos_totales, gano):
    try:
        # Obtiene la fecha y hora actual en formato "YYYY-MM-DD HH:MM:SS".
        fecha_juego = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Abre el archivo historial_adivinador.txt en modo "a" (append) para agregar contenido sin sobrescribir.
        with open("historial_adivinador.txt", "a", encoding="utf-8") as archivo:
            # Escribir el título y la fecha en el archivo
            archivo.write(f"*** Juego Adivinador - Fecha: {fecha_juego} ***\n")
            archivo.write(f"Intentos: {intentos_totales}/5\n")

            # Registra cada intento realizado con su número de intento y el número elegido por el jugador.
            for intento in intentos_realizados:
                archivo.write(f"Intento {intento[0]}: Número elegido: {intento[1]}\n")

            # Guardar si el jugador ganó o no
            archivo.write(f"Ganó?: {gano}\n")
            if not gano:
                # Si perdió, guardar el número a adivinar
                archivo.write(f"El número a adivinar era: {num_adivinar}\n")
            archivo.write("\n")
    except Exception as e:
        # Si ocurre un error al escribir en el archivo, lo notifica.
        print(f"Error al guardar el historial: {e}")


print("\t *** Juego del adivinador ***")
# Genera un número aleatorio entre 1 y 100 que el jugador deberá adivinar
num_adivinar = randint(1, 100)
# Inicializa el contador de intentos en 1
intentos = 1
gano = False
intentos_realizados = [] # Lista para registrar los intentos realizados por el jugador.

# Inicia un bucle que permite al jugador hasta 5 intentos para adivinar el número
while intentos <= 5:
    try:
        # Solicita al jugador que ingrese un número y lo convierte a entero
        num_jugador = int(input(f"Número de intento: {intentos}. Ingresa un número (1-100): "))

        # Registra el intento del jugador
        intentos_realizados.append((intentos, num_jugador))

        # Verifica si el número ingresado por el jugador es igual al número a adivinar
        if num_jugador == num_adivinar:
            # Si adivina correctamente, muestra un mensaje de felicitación y el número de intentos
            print(f"¡Felicidades!, adivinaste en {intentos} intentos.")
            gano = True
            # Guarda el historial con el resultado
            guardar_historial(intentos_realizados, intentos, gano)
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

    except ValueError:
        # Maneja la excepción si el jugador ingresa un valor que no es un número válido.
        print("E R R O R\n")
        print("Por favor, ingrese un número valido.")

# Después de 5 intentos, verifica si el jugador no ha adivinado el número
if intentos > 5 and not gano:
    # Muestra un mensaje de pérdida y revela el número a adivinar
    print(f"Perdiste. El número era: {num_adivinar}")
    # Guarda el historial con el resultado (en este caso, perdió)
    guardar_historial(intentos_realizados, intentos - 1, gano)
