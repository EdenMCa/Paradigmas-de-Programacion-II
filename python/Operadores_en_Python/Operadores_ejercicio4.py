"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 26 - 10 - 2024
Descripción: Este programa evalúa una expresión booleana a partir de cuatro entradas del usuario.
"""

print("\t *** Expresión booleana (exp1 O exp2) Y (exp3 O exp4)")

exp1 = (input("Ingresa un valor booleano (V/F): "))
# Se solicita al usuario que ingrese un valor booleano para la primera variable.
exp1 = exp1 == "V"
# Se convierte la entrada en un valor booleano verdadero o falso, dependiendo de si se ingresó "V".
exp2 = (input("Ingresa un valor booleano (V/F): "))
# Se solicita al usuario que ingrese un valor booleano para la segunda variable.
exp2 = exp2 == "V"
# Se convierte la entrada en un valor booleano verdadero o falso.
exp3 = (input("Ingresa un valor booleano (V/F): "))
# Se solicita al usuario que ingrese un valor booleano para la tercera variable.
exp3 = exp3 == "V"
# La entrada se convierte en un valor booleano.
exp4 = (input("Ingresa un valor booleano (V/F): "))
# Se solicita al usuario que ingrese un valor booleano para la cuarta variable.
exp4 = exp4 == "V"
# La entrada se convierte en un valor booleano.

resultado = (exp1 or exp2) and (exp3 or exp4)
# Se evalúa la expresión booleana combinando las entradas con operadores lógicos OR y AND.
# La expresión utiliza el operador OR (O) para evaluar (exp1 y exp2).
# Esto significa que el resultado será verdadero si al menos una de las dos (exp1 o exp2) es verdadera.
# Sucede lo mismo para (exp3 y exp4)
# Luego, se utiliza el operador AND (Y) para combinar el resultado anterior con la evaluación de exp3 y exp4.
# Esto significa que el resultado final será verdadero solo si ambos grupos de condiciones son verdaderos.
print(f"El resultado de la expresión booleana es: {resultado}")
