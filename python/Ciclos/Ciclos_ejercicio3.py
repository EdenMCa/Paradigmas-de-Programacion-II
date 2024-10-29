"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 25 - 10 -2024
Descripción: Este programa es una calculadora básica que permite realizar operaciones matemáticas simples como suma,
resta, multiplicación, división, división entera y exponenciación, de acuerdo a la operación que quiera realizar el
usuario. Cuenta con un menú y un ciclo while.
"""

print("\t *** CALCULADORA BÁSICA ***")

# Inicializamos la variable en 0, para que el ciclo while se ejecute al menos una vez.
op = 0
# El ciclo while que se ejecutará mientras la opción sea diferente de 7.
while op != 7:
    print("-----------------------------------")
    print("-           OPERACIONES           -")
    print("-                                 -")
    print("- [1].- SUMA                      -")
    print("- [2].- RESTA                     -")
    print("- [3].- MULTIPLICACIÓN            -")
    print("- [4].- DIVISIÓN                  -")
    print("- [5].- DIVISIÓN ENTERA           -")
    print("- [6].- EXPONENCIACIÓN            -")
    print("- [7].- SALIR                     -")
    print("-----------------------------------")

    # Solicitamos al usuario que ingrese la operación deseada.
    op = int(input("¿Qué operación desea realizar? "))

    # Si el usuario elige la opción 7, se termina el ciclo while.
    if op == 7:
        print("Saliendo del programa... :D")
    else:
        # Si el usuario quiere realizar una operación, le pedimos que ingrese dos númderos.
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        # Dependiendo de la opción elegida, se ejecuta el bloque de código correspondiente.
        if op == 1:
            # Realiza la suma y muestra el resultado
            print(f"La suma de los números: {numero1} + {numero2} es: {numero1 + numero2}")
        elif op == 2:
            # Realiza la resta y muestra el resultado
            print(f"La resta de los números: {numero1} - {numero2} es: {numero1 - numero2}")
        elif op == 3:
            # Realiza la multiplicación y muestra el resultado
            print(f"La multiplicación de los números: {numero1} * {numero2} es: {numero1 * numero2}")
        elif op == 4:
            # Indica al usuario que los números no deben ser cero y realiza la división
            print("Ingrese números diferentes a 0")
            print(f"La división de los números: {numero1} / {numero2} es: {numero1 / numero2}")
        elif op == 5:
            # Muestra un mensaje indicando que no debe ingresar un número 0.
            print("Ingrese números diferentes a 0")
            print(f"La división entera de los números: {numero1} // {numero2} es: {numero1 // numero2}")
        elif op == 6:
            # Realiza la exponenciación y muestra el resultado
            print(f"La exponenciación de los números: {numero1} ^ {numero2} es: {numero1 ** numero2}")
        else:
            # Si el usuario ingresa una opción que no se muestra en el menú, mostramos el siguiente mensaje.
            print("Opción no válida. Por favor, seleccione una opción del menú.")
    print()
    print()