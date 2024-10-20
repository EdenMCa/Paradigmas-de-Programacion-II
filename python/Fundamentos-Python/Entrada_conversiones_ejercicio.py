"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 20 - 10 - 2024
Descripción: Este programa permite ingresar información de los profesores de la UNSIJ, al final imprime esta información en un formato adecuado.
"""

print("A continuación, ingrese los datos que se le piden")
# Se imprime un mensaje que indica al usuario que debe ingresar los datos solicitados.

nombre_cadena = input("Ingrese su nombre completo: ")
# Este valor se almacena como una cadena de texto (string) en la variable 'nombre_cadena'.
no_cubiculo = int(input("Ingrese el número de cubículo en donde se encuetra: "))
# Se utiliza 'int()' para convertir el valor ingresado en una cadena a un número entero (int).
horas_clase = float(input("Ingrese el número de horas que imparte clases a la semana: "))
# La entrada se convierte a un número decimal (float) utilizando 'float()'.
bool_anos = input("¿Tiene más de 5 años en la UNSIJ? ")
# El valor ingresado se almacena como una cadena

bool_anos = bool_anos.lower() == "si"
# Se convierte el valor de 'bool_años' a minúsculas usando el método '.lower()'
# Luego se compara este valor con la cadena "si".
# La comparación devuelve 'True' si el usuario ingresó "si" y 'False' en caso contrario.
# Este resultado booleano se almacena nuevamente en 'bool_años'.
print(f"El profesor {nombre_cadena}, ubicado en el cubículo número {no_cubiculo} imparte un total de {horas_clase:.3f} horas de clases a la semana. Además, tiene más de 5 años en la unsij: {bool_anos}")
# .3f se utilizó para que las horas de clases se muestren con 3 decimales.