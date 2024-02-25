import pymysql
from datetime import datetime, timedelta


# Datos conexion
def conectar_bd():
    return pymysql.connect(host='localhost',
                           user='ferfong',
                           password='Developer123!',
                           database='lab_ing_software')



# Función para insertar registros en la tabla usuarios
def insertuser():
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            # Verificar si el correo electrónico ya existe
            correo = 'correo@example.com'
            cursor.execute("SELECT idUsuario FROM usuarios WHERE email = %s", (correo,))
            result = cursor.fetchone()
            if result:
                print("Ya existe un usuario con el correo electrónico proporcionado.")
            else:
                # Insertar el nuevo usuario
                sql = "INSERT INTO usuarios (nombre, apPat, apMat, password, email, superUser) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, ('Nombre', 'ApellidoPat', 'ApellidoMat', 'contraseña', correo, 0))
                connection.commit()
                print("Registros de usuarios insertados correctamente.")
    except Exception as e:
        print("Error al insertar registros de usuarios:", e)
    finally:
        connection.close()

# Función para insertar registros en la tabla peliculas
def insertpelis():
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            sql = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, ('Nombre de la película', 'Género', 120, 10))
        connection.commit()
        print("Registros de películas insertados correctamente.")
    except Exception as e:
        print("Error al insertar registros de películas:", e)
    finally:
        connection.close()

# Función para insertar registros en la tabla rentar
def insertrentas():
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            # Obtener el id del usuario insertado previamente
            cursor.execute("SELECT idUsuario FROM usuarios ORDER BY idUsuario DESC LIMIT 1")
            id_usuario = cursor.fetchone()[0]
            # Obtener el id de la película insertada previamente
            cursor.execute("SELECT idPelicula FROM peliculas ORDER BY idPelicula DESC LIMIT 1")
            id_pelicula = cursor.fetchone()[0]
            # Insertar registro en la tabla rentar
            sql = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (id_usuario, id_pelicula, datetime.now(), 7, 1))
        connection.commit()
        print("Registro de renta insertado correctamente.")
    except Exception as e:
        print("Error al insertar registro de renta:", e)
    finally:
        connection.close()


# Función para insertar registros en cada tabla
def insertregistros():
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            # Insertar registro en tabla peliculas
            sql = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, ('Nombre de la película', 'Género', 120, 10))

            # Obtener el id de la última película insertada
            id_pelicula = cursor.lastrowid

            # Insertar registro en tabla usuarios
            sql = "INSERT INTO usuarios (nombre, apPat, apMat, password, email, superUser) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, ('Nombre', 'ApellidoPat', 'ApellidoMat', 'contraseña', 'correo@example.com', 0))

            # Insertar registro en tabla rentar
            sql = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (1, id_pelicula, datetime.now(), 7, 1))

        connection.commit()
        print("Registros insertados correctamente.")
    except pymysql.IntegrityError as e:
        if e.args[0] == 1062:  # Código de error para duplicación de entrada
            print("Ya existe un usuario con el correo electrónico proporcionado.")
        else:
            print("Error al insertar registros:", e)
    finally:
        connection.close()


# Función para filtro para apellidos de usuarios
def filtroapellido(apellido):
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE apPat LIKE %s"
            cursor.execute(sql, ('%' + apellido,))
            result = cursor.fetchall()
            for row in result:
                print(row)
    except Exception as e:
        print("Error al filtrar usuarios:", e)
    finally:
        connection.close()


# Función para cambiar el género de una película
def jarochapelicula(nombre_pelicula, nuevo_genero):
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            # Verificar si la película existe
            sql = "SELECT * FROM peliculas WHERE nombre = %s"
            cursor.execute(sql, (nombre_pelicula,))
            result = cursor.fetchone()
            if result:
                # Actualizar el género de la película
                sql = "UPDATE peliculas SET genero = %s WHERE nombre = %s"
                cursor.execute(sql, (nuevo_genero, nombre_pelicula))
                connection.commit()
                print("Género de la película actualizado correctamente.")
            else:
                print("La película no existe.")
    except Exception as e:
        print("Error al cambiar el género de la película:", e)
    finally:
        connection.close()


# Función para eliminar rentas antiguas
def eliminantiguas():
    try:
        connection = conectar_bd()
        with connection.cursor() as cursor:
            fecha_limite = datetime.now() - timedelta(days=3)
            sql = "DELETE FROM rentar WHERE fecha_renta <= %s"
            cursor.execute(sql, (fecha_limite,))
            connection.commit()
            print("Rentas antiguas eliminadas correctamente.")
    except Exception as e:
        print("Error al eliminar rentas antiguas:", e)
    finally:
        connection.close()


# Ejecucion de las funciones
insertuser()
insertpelis()
insertrentas()
insertregistros()
filtroapellido('ApellidoPat')
jarochapelicula('Nombre de la película', 'Nuevo género')
eliminantiguas()