"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 27 - 10 - 2024
Descripción: El programa verifica si los usuarios del bar 'La Negra' cumplen los requisitos mínimos para entrar al bar.
"""

print("\t *** Acceso al bar 'La Negra' ***")

# Solicitamos al usuario su edad y convertimos el valor ingresado en un número entero.
edad = int(input("Ingrese tu edad: "))
# Solicitamos al usuario su presupuesto disponible y convertimos el valor ingresado en decimal (float).
presupuesto = float(input("Ingresa tu presupuesto: "))

print()
# Verifica si la edad ingresada es menor a 18.
if edad < 18:
    # Si la edad es menor a 18, se imprime el mensaje negando el acceso.
    print("Lo sentimos, ya estamos por cerrar.")
#Verifica si el presupuesto es menor a 250.
elif presupuesto < 250:
    # Si el presupuesto es insuficiente, también se indica que no puede ingresar.
    print("Lo sentimos, ya estamos por cerrar.")
#Si cumple con la edad y con el presupuesto permitido, se le da la bienvenida al bar.
else:
    print("¡Bienvenido a tu mejor bar!")