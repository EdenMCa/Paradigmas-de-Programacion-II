"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 23 - 10 -2024
Descripción: Este programa sirve para determinar la estación del año según el número del mes ingresado por el usuario, usando if-elif-else.
"""
print("\t Programa que determina la estación del año")
print()

# Solicita al usuario ingresar el número correspondiente al mes, y lo convertimos a entero.
num_mes = int(input("Ingresa el número del mes: "))

# La primera condición verifica si el mes está entre marzo (3) y mayo (5).
if num_mes >= 3 and num_mes <= 5:
    # Si la condición es verdadera, se imprime que la estación del mes ingresado es primavera.
    print(f"La estación del mes {num_mes} es primavera")
# Verifica si el mes está entre junio (6) y agosto (8) utilizando "elif" para verificar esta condición.
elif num_mes >= 6 and num_mes <= 8:
    # Si la condición es verdadera, se imprime que la estación del mes ingresado es verano.
    print(f"La estación del mes {num_mes} es verano")
# Verificamos si el mes está entre septiembre (9) y noviembre (11).
elif num_mes >= 9 and num_mes <= 11:
    # Si la condición es verdadera, se imprime que la estación del mes ingresado es otoño.
    print(f"La estación del mes {num_mes} es otoño")
# En esta condición verificamos si el mes es diciembre (12), enero (1) o febrero (2).
elif num_mes == 12 or num_mes == 1 or num_mes == 2:
    # Si la condición es verdadera, imprime que la estación del mes ingresado es invierno.
    print(f"La estación del mes {num_mes} es invierno")
# Si ninguna de las condiciones anteriores es verdadera, entonces no es posible que se trate de otro mes.
else:
    # Se imprime un mensaje de error indicando que el mes ingresado es incorrecto.
    print("\tE R R O R")
    print("Mes incorrecto")