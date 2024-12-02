"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 07 - 11 -2024
Descripción: Este programa realiza operaciones matemáticas básicas utilizando funciones en Python, fomentando la reutilización de código
"""
"""
Una función en Python es un bloque de código reutilizable que se define una vez y se puede llamar múltiples veces a lo 
largo de tu programa.

¿Por qué usar funciones?
- Reutilización de código: Evita repetir el mismo código una y otra vez.
- Modularidad: Divide un programa grande en partes más pequeñas y manejables.
- Abstracción: Oculta la complejidad de ciertas tareas, enfocándose en el nivel más alto del programa.
- Legibilidad: Hace que el código sea más fácil de leer y entender.

Sintaxis para crear una función:

# Se utiliza la palabra reservada def, el nombre y los parámetros que recibe (opcionales)
def nombre_funcion(parametro1, parametro2, ...):       
    # Código que realiza la función.
    
    return variable # Variable que retorna la función (opcional).
    
# Código a nivel de módulo -> que es lo que conocemos como código principal. 

Sintaxis:
    def nombre(parámetros):
        #Bloque de código
"""
# Función para mostrar el menú de operaciones
def menu ():
    print("-----------------------------------")
    print("-           OPERACIONES           -")
    print("-                                 -")
    print("- [1].- SUMA                      -")
    print("- [2].- RESTA                     -")
    print("- [3].- MULTIPLICACIÓN            -")
    print("- [4].- DIVISIÓN                  -")
    print("- [5].- DIVISIÓN ENTERA           -")
    print("- [6].- EXPONENCIACIÓN            -")
    print("- [0].- SALIR                     -")
    print("-----------------------------------")

# Función para realizar las operaciones matemáticas
def operaciones (numero_uno, numero_dos, opcion):
    # Verifica la operación seleccionada y ejecuta el cálculo correspondiente
    if op == 1:
        # Realiza la suma y muestra el resultado
        print(f"La suma de los números: {numero1} + {numero2} es: {numero1 + numero2:.2f}")
    elif op == 2:
        # Realiza la resta y muestra el resultado
        print(f"La resta de los números: {numero1} - {numero2} es: {numero1 - numero2:.2f}")
    elif op == 3:
        # Realiza la multiplicación y muestra el resultado
        print(f"La multiplicación de los números: {numero1} * {numero2} es: {numero1 * numero2:.2f}")
    elif op == 4:
        # Indica al usuario que los números no deben ser cero y realiza la división
        print("Ingrese números diferentes a 0")
        print(f"La división de los números: {numero1} / {numero2} es: {numero1 / numero2:.2f}")
    elif op == 5:
        # Muestra un mensaje indicando que no debe ingresar un número 0.
        print("Ingrese números diferentes a 0")
        print(f"La división entera de los números: {numero1} // {numero2} es: {numero1 // numero2:.2f}")
    elif op == 6:
        # Realiza la exponenciación y muestra el resultado
        print(f"La exponenciación de los números: {numero1} ^ {numero2} es: {numero1 ** numero2:.2f}")
    else:
        # Si el usuario ingresa una opción que no se muestra en el menú, mostramos el siguiente mensaje.
        print("Opción no válida. Por favor, seleccione una opción del menú.")
    return op
    # El ciclo while que se ejecutará mientras la opción sea diferente de 7.

# Variable para controlar el ciclo del programa
op = -1  # Inicializamos la variable para controlar el ciclo

# Ciclo principal que muestra el menú y ejecuta las operaciones seleccionadas
while op != 0:
    menu() # Llama a la función para mostrar el menú
        # Solicitamos al usuario que ingrese la operación deseada.
    op = int(input("¿Qué operación desea realizar? "))

    # Si el usuario elige la opción 7, se termina el ciclo while.
    if op == 0:
        print("Saliendo del programa... :D")

    elif 1 <= op <= 6:
        # Si la opción es válida, solicitamos los números para operar
        print()
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        # Llamamos a la función de operaciones
        operaciones(numero1, numero2, op)
    else:
        # Si la opción no es válida, mostramos un mensaje de error
        print("Opción no válida. Intente nuevamente.")
    print()  # Espacio para separar las iteraciones del menú