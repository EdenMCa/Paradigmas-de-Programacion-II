"""
Nombre: Rosendo Eden Mendoza Casarrubia
Fecha: 18 - 01 - 2025
Descripción: Este programa implementa el juego de "Piedra, Papel, Tijera, Lagarto, Spock", donde el jugador compite contra una CPU que elige sus
jugadas de forma aleatoria.
Cada partida se registra con los movimientos del jugador y la CPU, junto con el resultado y las estadísticas actuales.
Al finalizar el programa, el historial completo se guarda en un archivo de texto (historial_juego.txt) con la fecha y hora de la sesión.
"""

from random import randint # Importamos randint para generar números aleatorios (usado para la elección de la CPU).
from datetime import datetime # Importamos datetime para registrar la fecha y hora de las partidas.

# Diccionario de reglas del juego
juego = {
    "Piedra": ["Tijera", "Lagarto"],
    "Papel": ["Piedra", "Spock"],
    "Tijera": ["Papel", "Lagarto"],
    "Lagarto": ["Papel", "Spock"],
    "Spock": ["Tijera", "Piedra"]
}

# Contadores para las victorias del jugador, la CPU y empates
victorias_jugador = 0
victorias_cpu = 0
empates = 0

# Lista para registrar las partidas
partidas = []

# Función para mostrar las reglas del juego
def mostrar_reglas():
    print("\n*** Reglas del Juego: Piedra, Papel, Tijera, Lagarto, Spock ***")
    print("1. Piedra aplasta Tijera y destruye Lagarto.")
    print("2. Papel cubre Piedra y desaprueba Spock.")
    print("3. Tijera corta Papel y decapita Lagarto.")
    print("4. Lagarto come Papel y envenena Spock.")
    print("5. Spock destruye Tijera y vaporiza Piedra.")
    print("6. Si ambos jugadores eligen lo mismo, es un empate.")
    print("7. La CPU elige una opción de forma aleatoria.")

# Función para guardar el historial en un archivo
def guardar_historial(partidas):
    try:
        # Obtener la fecha actual en formato adecuado
        fecha_juego = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("historial_juego.txt", "a", encoding="utf-8") as archivo:
            archivo.write("\n")
            archivo.write(f"*** Piedra, papel, tijera, lagarto, spock - Fecha: {fecha_juego} ***\n")
            archivo.write("\n")
            # Iteramos por cada partida y escribimos los detalles en el archivo.
            for partida in partidas:
                archivo.write(
                    f"Jugador: {partida['jugador']}, CPU: {partida['cpu']}, Resultado: {partida['resultado']}\n"
                    f"Victorias del jugador: {partida['victorias_jugador']}, "
                    f"Empates: {partida['empates']}, "
                    f"Victorias del CPU: {partida['victorias_cpu']}\n\n"
                )
    # Mostramos un mensaje de error si ocurre algún problema al guardar el archivo.
    except Exception as e:
        print(f"Error al guardar el historial: {e}")

# Inicializamos la variable opcion_elegida en -1 para que entre al ciclo al menos una vez
opcion_elegida = -1

while opcion_elegida != 0:
    print()
    print("\t *** Juego de Piedra, Papel, Tijera, Lagarto, Spock ***")
    # Muestra las estadísticas del jugador
    print(f"Victorías del jugador: {victorias_jugador}, Empates: {empates}, Victorías del CPU: {victorias_cpu}")
    print()

    print("-----------------------------------")
    print("-                                 -")
    print("- [1].- Piedra                    -")
    print("- [2].- Papel                     -")
    print("- [3].- Tijera                    -")
    print("- [4].- Lagarto                   -")
    print("- [5].- Spock                     -")
    print("- [6].- Ver reglas                -")
    print("- [0].- Salir                     -")
    print("-----------------------------------")
    print()

    # Solicitamos al jugador que seleccione una opción. En caso de error, manejamos el valor ingresado.
    try:
        opcion_elegida = int(input("Seleccione una opción: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        continue # Si hay un error, volvemos al inicio del ciclo.

    if opcion_elegida == 6:  # Mostrar reglas
        mostrar_reglas()

    elif 1 <= opcion_elegida <= 5:  # Jugar
        cpu = randint(1, 5)  # Opción aleatoria para la CPU

        # Lista de opciones para traducir los números a palabras
        opciones = ["Piedra", "Papel", "Tijera", "Lagarto", "Spock"]
        op_jugador = opciones[opcion_elegida - 1]
        op_cpu = opciones[cpu - 1]

        if op_jugador == op_cpu:
            resultado = "empate"
            empates += 1
        elif op_cpu in juego[op_jugador]:
            resultado = "victoria"
            victorias_jugador += 1
        else:
            resultado = "derrota"
            victorias_cpu += 1

        # Mostrar el resultado de la ronda
        print(f"Jugador: {op_jugador}. CPU: {op_cpu}. El resultado es {resultado}.")

        # Registrar la partida
        partidas.append({
            "jugador": op_jugador,
            "cpu": op_cpu,
            "resultado": resultado,
            "victorias_jugador": victorias_jugador,
            "empates": empates,
            "victorias_cpu": victorias_cpu
        })

    elif opcion_elegida == 0:  # Salir del programa
        # Guardar el historial completo al salir
        guardar_historial(partidas)
        print("Saliendo del programa... c:")
    else:
        print("Opción no válida, intente de nuevo.")

