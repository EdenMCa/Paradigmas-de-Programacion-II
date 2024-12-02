"""
Nombre: Mendoza Casarrubia Rosendo Eden
Fecha: 14 - 11 -2024
Descripción: Este código es un ejemplo básico para trabajar con diccionarios.
"""
"""
Diccionario:
    -> Desordenados
    -> Inmutables   
    -> Se almacenan en forma de key-valor
"""
"""
Sintaxis:
    diccionario = {'Key1': valor1, 'Key2': valor2}
"""
# Se crea un diccionario llamado 'profesor' que contiene la siguiente información:
# 'nombre' es la clave para el valor 'Alberto', 'correo' es la clave para el valor 'alberto.mtba@unsij',
# y 'cubo' es la clave para el valor 12.
profesor = {'nombre': "Alberto", 'correo': "alberto.mtba@unsij", 'cubo': 12}
print(profesor) # Imprimimos el diccionario 'profesor' en su totalidad.
print()
# Usamos el metodo 'get()' para obtener el valor asociado con la clave 'correo' en el diccionario 'profesor'.
correo = profesor.get("correo")
# Accedemos directamente al valor asociado con la clave 'cubo' usando los corchetes.
cubo = profesor["cubo"]
# Se imprime el valor de la variable 'correo', que contiene el correo del profesor.
print(correo)
# Se imprime el valor de la variable 'cubo', que contiene el número 12.
print(cubo)