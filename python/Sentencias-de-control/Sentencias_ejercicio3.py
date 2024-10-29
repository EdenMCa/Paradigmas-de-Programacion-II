"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 27 - 10 - 2024
Descripción: El programa calcula un descuento basado en la cantidad comprada y si el usuario tiene o no membresía.
Si tiene membresía, el descuento es del 5% para compras menores a 1000 y del 8% para compras iguales o superiores
a 1000. Si no tiene membresía, se le invita a obtener una para futuros descuentos.
"""
print("\t *** Descuentos por ser miembros de 'La cona' ***")
# Solicita al usuario el monto de su compra y convierte el valor ingresado en un número decimal (float).
compra = float(input("Ingrese la cantidad comprada: "))
# Le preguntamos al usuario si tiene una membresía y convierte la respuesta a un valor booleano.
membresia = input("¿Cuenta con membresía? (si/no): ")
# La variable membresia será True si el usuario responde "si" y False en cualquier otro caso.
membresia = membresia == "si"

print()
#Verifica si el usuario tiene membresía y su compra es menor a 1000.
if membresia and compra < 1000:
    # Si ambas condiciones se cumplen, se aplica un descuento del 5%.
    print("Tu descuento es del 5 %")
    # Calcula el total aplicando el 5% de descuento y lo muestra con dos decimales.
    print(f"El total es de $ {compra * 0.95:.2f}")
# Verifica si el usuario tiene membresía y su compra es igual o mayor a 1000.
elif membresia and compra >= 1000 :
    # Si ambas condiciones se cumplen, se aplica un descuento del 8%.
    print("Tu descuento es del 8 %")
    # Calcula el total aplicando el 8% de descuento y lo muestra con dos decimales.
    print(f"El total es de $ {compra * 0.92:.2f}")
# Si ninguna de las condiciones se cumplen, entonces el usuario no tiene membresía.
else:
    # Informamos al usuario los beneficios de obtener una membresía para futuros descuentos.
    print("Se te invita a ser miembro de la tienda para obtener un descuento de hasta el 8 %")
    # Muestra el total sin descuento, ya que no se aplica ninguno en este caso.
    print(f"El total es de $ {compra:.2f}")
