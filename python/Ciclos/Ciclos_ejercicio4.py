"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 25 - 10 -2024
Descripción:
"""

print("\tBienvenido a tu cuenta de Banco Azteca")

# Iniciamos la variable op en -1 para que entremos al bucle al menos una vez.
op = -1
# Inicializamos el saldo en 0, que es el que guardara nuestros movimientos de dinero.
saldo = 0

# Iniciamos el ciclo while, que nos permitirá realizar múltiples operaciones hasta que el usuario decida salir.
while op != 0:
    # Imprimimos el menú de opciones para que el usuario pueda seleccionar una operación.
    print("-----------------------------------")
    print("-                                 -")
    print("- [1].- Consultar tu saldo        -")
    print("- [2].- Ingresar dinero           -")
    print("- [3].- Retirar dinero            -")
    print("- [0].- Salir                     -")
    print("-----------------------------------")

    # Solicitamos al usuario que seleccione una opción del menú.
    # Lo guardamos en la variable op como entero.
    op = int(input("Seleccione una opción: "))

    # Si elige consultar saldo, entraremos en este bloque de código.
    if op == 1:
        print(f"Su saldo actual es de ${saldo:.2f}.")
    # Si el usuario elige ingresar dinero, entraremos en este bloque de código.
    elif op == 2:
        # Solicitamos al usuario la cantidad a depositar.
        ingreso = float(input("Ingrese la cantidad a depositar: "))
        # Sumamos el monto ingresado al saldo actual.
        saldo += ingreso
        # Mostramos un mensaje indicando que se ha realizado el depósito.
        print(f"Ha ingresado ${ingreso} a su cuenta. Su saldo actual es de $ {saldo:.2f}")
    # Opción para retirar dinero de la cuenta.
    elif op == 3:
        # Solicitamos al usuario la cantidad que desea retirar.
        retiro = float(input("Ingrese la cantidad a retirar: "))
        # Verificamos si el saldo es suficiente para realizar el retiro.
        if retiro <= saldo:
            # Si el saldo es suficiente, restamos el monto retirado al saldo actual.
            saldo -= retiro
            print(f"Ha retirado ${retiro} de su cuenta.")
        # Si el saldo no es suficiente, no podemos realizar el retiro.
        else:
            print("Fondos insuficientes para realizar esta operación.")
    # Opción para salir del programa.
    elif op == 0:
        # Mostramos un mensaje de despedida.
        print("Gracias por usar Banco Azteca. ¡Hasta luego!")
    # Si el usuario selecciona una opción no válida, mostramos un mensaje de error.
    else:
        print("E R R O R")
        print("Opción no válida. Por favor, seleccione una opción del menú.")
    print()