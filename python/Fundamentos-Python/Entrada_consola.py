'''
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 20 - 10 - 2024
Descripción: Entrada de datos por consola para interacturar con el usuario con valores dinámicos.
'''

# Comentar sobre la función input.
# La función 'input()' permite al usuario ingresar un valor desde la consola.
# Siempre devuelve una cadena de texto (string), sin importar lo que el usuario ingrese.
# Esto significa que aunque el usuario ingrese un número, Python lo interpreta inicialmente como una cadena.
# Por eso, el valor se almacena en la variable 'numero1_cadena' como un string.
numero1_cadena = input("Introduce un número decimal: ")
numero2_cadena = input("Introduce otro número decimal: ")
resultado_cadena = numero1_cadena + numero2_cadena # Verificar qué es lo que realiza esta instrucción (ver el print).
print()
print(" ****  Recibir número sin un casting de varibles  ****")
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}")
# Si el usuario ingresó "3" y "4", el resultado será "34", ya que '+' entre cadenas concatena los valores.


# Comentar por qué se realiza el casting de variables.
# Aquí se utiliza la función 'float()' para convertir el string almacenado en 'numero1_cadena' y 'numero2_cadena',
# en un número decimal (float). Esto es necesario para que podamos realizar operaciones matemáticas con él.
# Si el usuario ingresó "2.7", se convierte en el número 2.7.
numero1_float = float(numero1_cadena)
numero2_float = float(numero2_cadena)
resultado_float = numero1_float + numero2_float # Verificar qué es lo que realiza de esta manera y compáralo.
print()
print(" ****  Casting de varibles  ****")
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}") #Gracias al casting podemos realizar la suma.
# El resultado que obtendremos será 7.0, en vez de 34.