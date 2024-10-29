"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 27 - 10 - 2024
Descripción: Este programa calcula el costo total de un tour turístico en Ecoturixtlán. Ofrece un descuento
en ciertos días de la semana y calcula el total según el número de adultos y niños en el grupo.
"""
print("\t *** Tour turístico Ecoturixtlán ***")

# Se define el precio del tour para adultos.
precio_adultos = 200.0
# Se define el precio del tour para niños.
precio_ninos = 100.0

# Se solicita el nombre del cliente y se almacena en la variable 'cliente'.
cliente = input("Ingresa el nombre de cliente: ")
# Se solicita el número de adultos que asistirán al tour y se almacena como un número entero.
adultos = int(input("Ingresa el número de adultos: "))
# Se solicita el número de niños que asistirán al tour y se almacena como un número entero.
ninos = int(input("Ingresa el número de niños: "))
# Se solicita el día de la semana en el que se tomará el tour y se almacena en la variable 'dia'.
dia = input("Ingresa el dia de la semana: ")

# Se verifica si el día es uno de los días con descuento (lunes, martes o jueves) y almacena el resultado en 'descuento'.
descuento = dia in ("lunes", "martes", "jueves")

#Se verifica si el cliente vino un dia con descuento.
if descuento:
    # Si hay descuento, se calcula el total con un 10% de descuento y se muestra el costo total al cliente.
    print(f"Gracias por tu visita {cliente} este día {dia}. El costo total es de $ {((adultos * precio_adultos) + (ninos * precio_ninos)) * 0.90:.2f}")
else:
    # Si no hay descuento, se calcula el total sin descuento y se muestra el costo total al cliente.
    print(f"Gracias por tu visita {cliente} este día {dia}. El costo total es de $ {(adultos * precio_adultos) + (ninos * precio_ninos):.2f}")