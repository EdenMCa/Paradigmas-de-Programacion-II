"""
Nombre: Rosendo Eden Mendoza Casarrubia
Fecha: 18 - 01 - 2025
Descripción: Este programa es una aplicación de rifa en la que los participantes pueden registrarse con sus correos electrónicos, y luego se seleccionan
aleatoriamente uno o más ganadores. El usuario interactúa con el programa a través de un menú de opciones, donde puede ver los participantes, agregar
nuevos correos, eliminar correos, seleccionar ganadores aleatorios, y ver los ganadores de rifas anteriores.
Después de seleccionar a los ganadores, el programa guarda el historial de la rifa en un archivo de texto llamado ganadores.txt. Este historial incluye:
La fecha y hora en que se realizaron las selecciones de ganadores.
Los correos electrónicos de los ganadores seleccionados.
El programa maneja errores de entrada, como el ingreso de una opción no válida o la selección de más ganadores que participantes disponibles. Además,
utiliza un conjunto para almacenar los correos electrónicos de los participantes, asegurando que no haya correos duplicados. Los ganadores seleccionados
se guardan de manera persistente en el archivo ganadores.txt, lo que permite consultar los ganadores de rifas anteriores.
"""
import random # Importamos randint para generar un número aleatorio entre 1 y 100.
from datetime import datetime # Importamos datetime para registrar la fecha y hora.

# Función para mostrar el menú de opciones disponibles.
def menu():
    print("---------------------------------------------------")
    print("-             RIFA DE UNA COMPUTADORA             -")
    print("-                                                 -")
    print("- [1].- Ver correos de participantes.             -")
    print("- [2].- Agregar correo de participante.           -")
    print("- [3].- Eliminar correo de participante.          -")
    print("- [4].- Seleccionar ganadores.                    -")
    print("- [5].- Ver ganadores anteriores.                 -")
    print("- [0].- Salir                                     -")
    print("---------------------------------------------------")


# Función para ver los correos de los participantes.
def ver_correos(participantes):
    # Verifica si hay participantes registrados en el conjunto.
    if participantes:
        print("\nCorreos de los participantes:")
        # Si existen, muestra cada uno junto con su índice.
        # Utilizamos 'enumerate' para recorrer 'participantes' y obtener tanto el índice (i) como el correo.
        # 'enumerate' se usa para agregar un índice a cada correo, lo que permite numerar los correos de forma automática
        # y mostrar al usuario un listado ordenado desde el 1, gracias a 'start=1' (el valor de inicio del índice).
        for i, correo in enumerate(participantes, start=1):
            print(f"{i}. {correo}")
    else:
        # Si no hay participantes, muestra el siguiente mensaje.
        print("\nNo hay participantes para mostrar.")


# Función para agregar un correo de participante.
def agregar_correo(participantes):
    # Solicita al usuario que ingrese el correo del nuevo participante.
    correo = input("\nIngrese el correo electrónico del participante: ")
    # Verifica si el correo ya está en la lista de participantes.
    if correo in participantes:
        print("El correo ya está registrado. Intente con otro.")
    else:
        # Si el correo no está registrado, lo agrega al conjunto de participantes.
        participantes.add(correo)
        print(f"El correo {correo} se ha agregado correctamente.")


# Función para eliminar un correo de participante.
def eliminar_correo(participantes):
    # Verifica si hay participantes registrados antes de continuar.
    if participantes:
        # Muestra los correos actuales para que el usuario seleccione uno para eliminar.
        ver_correos(participantes)
        # Solicita el correo que el usuario desea eliminar.
        correo = input("\nIngrese el correo electrónico que desea eliminar: ")
        # Verifica si el correo está en la lista de participantes.
        if correo in participantes:
            # Si el correo está en la lista, lo elimina.
            participantes.remove(correo)
            print(f"El correo {correo} se ha eliminado correctamente.")
        else:
            # Si el correo no está registrado, mostramos un mensaje de error.
            print("El correo no está registrado.")
    else:
        # Si no hay participantes, mostramos un mensaje informando que no hay correos para eliminar.
        print("\nNo hay participantes registrados para eliminar.")


# Función para seleccionar múltiples ganadores.
def seleccionar_ganadores(participantes):
    if participantes:
        try:
            # Solicita al usuario cuántos ganadores quiere seleccionar.
            num_ganadores = int(input("\nIngrese la cantidad de ganadores que desea seleccionar: "))
            # Si el número de ganadores es mayor que los participantes, muestra un error.
            if num_ganadores > len(participantes):
                print("La cantidad de ganadores excede el número de participantes.")
                return
            # Convierte el conjunto de participantes a lista para poder usarlo con random.sample.
            lista_participantes = list(participantes)
            # Selecciona aleatoriamente la cantidad de ganadores indicada.
            ganadores = random.sample(lista_participantes, num_ganadores)
            print("\n¡Ganadores seleccionados!")
            for ganador in ganadores:
                print(f"- {ganador}")

            # Obtener la fecha actual en formato adecuado
            fecha_juego = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Abre el archivo "ganadores.txt" en modo de escritura (añadir) para guardar los ganadores.
            with open("ganadores.txt", "a", encoding="utf-8") as archivo:
                archivo.write("\n")
                archivo.write(f"Ganadores seleccionados - Fecha: {fecha_juego}\n")
                # Escribe los ganadores en el archivo.
                for ganador in ganadores:
                    archivo.write(f"{ganador}\n")
            print("Los ganadores han sido guardados en 'ganadores.txt'.")
        except ValueError as e:
            # Si el valor ingresado no es un número entero, muestra un mensaje de error.
            print(f"Error: Ingrese un número válido. {e}")
    else:
        print("\nNo hay participantes registrados para la rifa.")


# Función para ver los ganadores anteriores.
def ver_ganadores():
    try:
        # Intenta abrir el archivo "ganadores.txt" en modo lectura.
        with open("ganadores.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            # Si el archivo no está vacío, muestra los ganadores registrados.
            if contenido.strip():
                print("\nGanadores anteriores:")
                print(contenido)
            else:
                print("\nNo hay ganadores registrados aún.")
    except FileNotFoundError as e:
        # Si el archivo no existe (porque aún no se ha guardado ganadores), muestra un error.
        print(f"\nEl archivo 'ganadores.txt' no existe. Aún no se han registrado ganadores. {e}")


# Menú principal
participantes = set()

# Inicializamos la variable opcion
opcion = -1
# Inicia un bucle que continuará hasta que el usuario seleccione la opción '0' (Salir).
while opcion != 0:
    menu()
    try:
        # Solicita al usuario que ingrese una opción del menú.
        opcion = int(input("\nSeleccione una opción: "))
        # Dependiendo de la opción seleccionada, llama a la función correspondiente.
        if opcion == 1:
            ver_correos(participantes) # Muestra los correos de los participantes.
        elif opcion == 2:
            agregar_correo(participantes) # Permite agregar un correo a la lista de participantes.
        elif opcion == 3:
            eliminar_correo(participantes) # Permite eliminar un correo de los participantes.
        elif opcion == 4:
            seleccionar_ganadores(participantes) # Selecciona ganadores de la rifa.
        elif opcion == 5:
            ver_ganadores() # Muestra los ganadores anteriores.
        elif opcion == 0:
            print("Saliendo del programa... :D")
        else:
            # Informa si la opción seleccionada no es válida.
            print("Opción no válida. Intente de nuevo.")
    except ValueError:
        # Si el usuario ingresa un valor no válido (que no sea un número), muestra un error.
        print("Error: Ingrese un número válido.")