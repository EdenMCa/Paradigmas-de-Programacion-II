'''
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 20 - 10 - 2024
Descripción: Conversión de cadenas a int, float y boolean mediante la interacción con consola.
'''

# Comentar sobre las funciones anidadas.
# El término "anidado" a menudo se asocia con una estructura de funciones dentro de funciones
# (como definir una función dentro de otra). En este caso, aunque estamos utilizando input() dentro de int(),
# el enfoque es más sobre composición de funciones que sobre anidamiento en sí.
print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ")
semestre = int(input("Ingresa el no. de semestre: "))
promedio = float(input("Ingresa el promedio: "))
es_mujer = input("¿Es mujer (Si/No)?: ")

# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si"

# Se imprimen los datos del alumno.
# Comentar  qué es lo que realiza {promedio:.2f} probando con números diferentes.
# La expresión {promedio:.2f} es una forma de formateo de cadenas en Python que permite controlar cómo se presenta un número decimal en la salida.
# :.2f Esto es un especificador de formato que indica cómo debe presentarse el valor.
#: Introduce la parte de formato de la especificación.
# .2: Indica que se debe mostrar exactamente 2 dígitos después del punto decimal, si nosotros cambiamos el número por cualquier otro solo va a modificar cuantos número apareceran despúes del punto.
# f: Indica que se trata de un número en formato de punto flotante (float).
print()
print(f"El alumno {nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")