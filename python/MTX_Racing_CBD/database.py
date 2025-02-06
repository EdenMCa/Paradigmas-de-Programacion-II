from mysql.connector import pooling, Error, connect

class Conexion:
    pool = None

    @classmethod
    def get_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    host = "localhost",
                    user = "root",
                    password = "root",
                    database = "historial",
                    pool_name = "DB_historial_pool",
                    pool_size = 3,
                    ssl_disabled = True
                )
                print("Pool creado")
            except Error as e:
                print(f"Error al crear el pool: {e}")
        return cls.pool

    @classmethod
    def get_connection(cls):
        return cls.get_pool().get_connection()

def guardar_puntuacion(nombre, puntuacion):
    conn = Conexion.get_connection()
    try:
        cursor = conn.cursor()
        query = "INSERT INTO puntuaciones (nombre, puntuacion) VALUES (%s, %s)"
        cursor.execute(query, (nombre, puntuacion))
        conn.commit()
        print(f"Puntuación de {nombre} guardada con éxito: {puntuacion}")
    except Error as e:
        print(f"Error al guardar la puntuación: {e}")
    finally:
        try:
            cursor.close()
        except Exception as ex:
            print("Error cerrando el cursor:", ex)
        try:
            conn.close()
        except Exception as ex:
            print("Error cerrando la conexión:", ex)

# Función de prueba (opcional)
if __name__ == "__main__":
    # Verificar que la conexión funcione
    try:
        conn = Conexion.get_connection()
        if conn.is_connected():
            print("Conexión exitosa a la base de datos.")
        conn.close()
    except Error as e:
        print("Error al probar la conexión:", e)

    # Probar inserción
    guardar_puntuacion("Prueba", 100)
