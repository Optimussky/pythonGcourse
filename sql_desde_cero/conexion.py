# connection to sqlite

import sqlite3

conexion = sqlite3.connect("basepruebacurso.db")
cursor = conexion.cursor()

def obtener_clientes():
    sql = "SELECT * FROM clientes;"
    cursor.execute(sql)
    clientes = cursor.fetchall()
    #print(clientes)
    #print(clientes[0])
    #print(clientes[0][1])

    #for cliente in clientes:
    #    print(cliente)

    for cliente in clientes:
        print(cliente[2])


def agregar_cliente(nombre, apellido, email, fecha_registro, rol, telefono="NULL"):
    cliente = (
            nombre,
            apellido,
            email, 
            fecha_registro,
            telefono,
            rol
            )

    sql = f"INSERT INTO clientes (nombre, apellido, email, fecha_registro, telefono, rol) VALUES {cliente}"
    cursor.execute(sql)


def obtener_un_cliente(id):
    sql = f"SELECT * FROM clientes WHERE id = {id}"
    cursor.execute(sql)
    cliente = cursor.fetchone()
    print(cliente)

def editar_un_cliente(id,nombre):
    sql = f"UPDATE clientes SET nombre = 'nombre' WHERE id = {id}"
    cursor.execute(sql)

def eliminar_cliente(id):
    sql = f"DELETE FROM clientes WHERE id = {id}"
    cursor.execute(sql)

#obtener_clientes()
agregar_cliente("Pia", "Mendez", "correo@gmail.com", "2022-07-29 18:32:01","cliente")


conexion.commit()
conexion.close()
