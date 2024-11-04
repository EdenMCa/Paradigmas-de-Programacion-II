"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 29 - 10 -2024
Descripción: Este programa permite al usuario calcular el área y perímetro de un rectángulo y un círculo.
De acuerdo con un menú que itera gracias al while.
"""

print("\t *** Programa que calcula el área y perímetro *** ")

opcion_elegida = -1 # Inicializamos la variable opcion_elegida en -1 para poder entrar al ciclo
pi = 3.1416 # Definimos la constante pi

# Comienza un ciclo que se repetirá hasta que el usuario elija salir
while opcion_elegida != 0:
    print("---------------------------------------------------")
    print("-                   OPERACIONES                   -")
    print("-                                                 -")
    print("- [1].- Calcular el área de un rectángulo         -")
    print("- [2].- Calcular el perímetro de un rectángulo    -")
    print("- [3].- Calcular el área de un circulo            -")
    print("- [4].- Calcular el perímetro de un círculo       -")
    print("- [0].- Salir                                     -")
    print("---------------------------------------------------")
    print()
    # Solicita al usuario que seleccione una opción y lo guarda como entero
    opcion_elegida = int(input("Seleccione una opción: "))

    if opcion_elegida == 1: # Si el usuario elige la opción 1, se calcula el área de un rectángulo
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        # Calcula el área de acuerdo a la formula y muestra el área del rectángulo
        print(f"El área del rectángulo es: {base * altura:.3f}")
    elif opcion_elegida == 2: # Si el usuario elige la opción 2, se calcula el perímetro de un rectángulo
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        # Calcula y muestra el perímetro del rectángulo
        print(f"El perímetro del rectángulo es: {(base + altura) * 2:.3f}")
    elif opcion_elegida == 3: # Si el usuario elige la opción 3, se calcula el área de un círculo
        radio = float(input("Ingrese el radio del círculo: "))
        # Calcula y muestra el área del círculo
        print(f"El área del círculo es: {pi * radio ** 2 :.3f}")
    elif opcion_elegida == 4:# Si el usuario elige la opción 4, se calcula el perímetro de un círculo
        radio = float(input("Ingrese el radio del círculo: "))
        # Calcula y muestra el perímetro del círculo
        print(f"El perímetro del círculo es: {(radio * 2) * pi:.3f}")
    elif opcion_elegida == 0:# Si el usuario elige la opción 0, termina el ciclo
        print("Saliendo del programa... c:")
    else: # Si el usuario ingresa una opción no válida, se muestra un mensaje de error
        print("Opción no válida")

    print()



