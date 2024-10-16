"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 12 - 10 - 2024
Descripción: El programa realiza conversiones entre números y cadenas, así como evaluaciones de sus valores booleanos.
"""

num_str = [str(3.14159265), str(12), str(0)] #Convierte números a cadenas
#num_str contiene las cadenas de los números

num_bool = [bool(3.14159265), bool(12), bool(0)] #Indica el valor booleano de las números
#En python, el número 0 es considerado false por lo tanto todos los números diferentes a cero son true

num = [int("10002"), float("100.02"), int("0")] #COnvierte las cadenas a números.

val_bool = [bool(int("10002")), bool(float("100.02")), bool(int("0"))] #Se indica el valor booleano de las cadenas iniciales

#Se imprimen las variables
print(num_str)
print(num_bool)
print(num)
print(val_bool)