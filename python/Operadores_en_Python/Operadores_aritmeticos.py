"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 17 - 10 - 2024
Descripción: Este programa realiza operaciones aritméticas básicas entre dos números ingresados por el usuario.
Incluye suma, resta, división, multiplicación, módulo, potencia y división entera.

"""

print("Ingrese dos números")

num_uno = int(input("Ingrese un número entero: "))
# Se solicita el primer número al usuario, lo convierte a entero y lo almacena en la variable 'num_uno'
# La función int() antes del input, convierte la entrada de texto a un tipo de dato entero, esto es necesario para operaciones aritméticas.

num_dos = int(input("Ingrese un número entero: "))
# Obtiene el segundo número del usuario, lo convierte a entero y lo almacena en la variable 'num_dos'.

suma_num = num_uno + num_dos
# Realiza la suma de los dos números y almacena el resultado en suma_num.
resta_num = num_uno - num_dos
# Realiza la resta de num_uno menos num_dos y almacena el resultado en resta_num.
div_num = num_uno / num_dos
# Realiza la división de num_uno entre num_dos y almacena el resultado en div_num.
mul_num = num_uno * num_dos
# Realiza la multiplicación de num_uno por num_dos y almacena el resultado en mul_num.
mod_num = num_uno % num_dos
# Calcula el módulo de num_uno y num_dos, almacenando el residuo de la división en mod_num.
exponenciacion_num = num_uno ** num_dos
# Calcula la potencia de num_uno elevado a num_dos y almacena el resultado en exponenciacion_num.
div_entera_num = num_uno // num_dos
# Realiza la división entera de num_uno entre num_dos y almacena el resultado en div_entera_num.


# Se imprime el resultado de cada operación con mensajes descriptivos para una mejor organizacióna.
print(f"El resultado de la suma del número {num_uno} y {num_dos} es: {suma_num}")
print(f"El resultado de la resta del número {num_uno} y {num_dos} es: {resta_num}")
print(f"El resultado de la división del número {num_uno} y {num_dos} es: {div_num:.3f}") # Muestra el resultado de la división con tres decimales
print(f"El resultado de la multiplicación del número {num_uno} y {num_dos} es: {mul_num}")
print(f"El resultado del módulo del número {num_uno} y {num_dos} es: {mod_num}")
print(f"El resultado de la  del número {num_uno} y {num_dos} es: {exponenciacion_num}")
print(f"El resultado de la división entera del número {num_uno} y {num_dos} es: {div_entera_num}")


