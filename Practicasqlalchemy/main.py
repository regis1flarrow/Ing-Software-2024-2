from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Usuario, Pelicula, Rentar

# Configura la conexión a la base de datos
engine = create_engine('sqlite:///tu_base_de_datos.db')
Session = sessionmaker(bind=engine)
session = Session()


def ver_registros(tabla):
    registros = session.query(tabla).all()
    for registro in registros:
        print(registro)


def filtrar_por_id(tabla, id):
    registro = session.query(tabla).filter_by(id=id).first()
    if registro:
        print(registro)
    else:
        print("No se encontró ningún registro con ese ID.")


def actualizar_nombre_renta(id, nuevo_nombre):
    renta = session.query(Rentar).filter_by(id=id).first()
    if renta:
        renta.nombre = nuevo_nombre
        session.commit()
        print("Nombre de la renta actualizado correctamente.")
    else:
        print("No se encontró ninguna renta con ese ID.")


def eliminar_registro(tabla, id=None):
    if id:
        registro = session.query(tabla).filter_by(id=id).first()
        if registro:
            session.delete(registro)
            session.commit()
            print("Registro eliminado correctamente.")
        else:
            print("No se encontró ningún registro con ese ID.")
    else:
        confirmacion = input("¿Está seguro que desea eliminar todos los registros de esta tabla? (s/n): ")
        if confirmacion.lower() == 's':
            session.query(tabla).delete()
            session.commit()
            print("Todos los registros fueron eliminados correctamente.")


def mostrar_menu():
    print("Menú:")
    print("1. Ver los registros de una tabla.")
    print("2. Filtrar los registros de una tabla por ID.")
    print("3. Actualizar la columna nombre de un registro de la tabla Renta.")
    print("4. Eliminar un registro por ID o todos los registros.")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            tabla = input("Ingrese el nombre de la tabla (Usuario, Pelicula, Rentar): ")
            if tabla == 'Usuario':
                ver_registros(Usuario)
            elif tabla == 'Pelicula':
                ver_registros(Pelicula)
            elif tabla == 'Rentar':
                ver_registros(Rentar)
            else:
                print("Tabla no válida.")

        elif opcion == '2':
            tabla = input("Ingrese el nombre de la tabla (Usuario, Pelicula, Rentar): ")
            id = int(input("Ingrese el ID del registro a filtrar: "))
            if tabla == 'Usuario':
                filtrar_por_id(Usuario, id)
            elif tabla == 'Pelicula':
                filtrar_por_id(Pelicula, id)
            elif tabla == 'Rentar':
                filtrar_por_id(Rentar, id)
            else:
                print("Tabla no válida.")

        elif opcion == '3':
            id = int(input("Ingrese el ID de la renta a actualizar: "))
            nuevo_nombre = input("Ingrese el nuevo nombre para la renta: ")
            actualizar_nombre_renta(id, nuevo_nombre)

        elif opcion == '4':
            tabla = input("Ingrese el nombre de la tabla (Usuario, Pelicula, Rentar): ")
            id = input("Ingrese el ID del registro a eliminar (dejar en blanco para eliminar todos): ")
            if id:
                id = int(id)
            if tabla == 'Usuario':
                eliminar_registro(Usuario, id)
            elif tabla == 'Pelicula':
                eliminar_registro(Pelicula, id)
            elif tabla == 'Rentar':
                eliminar_registro(Rentar, id)
            else:
                print("Tabla no válida.")

        elif opcion == '5':
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
