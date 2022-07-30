# sql.py CRUD pequeño backend
# Administrar un negocio de catalogo de peliculas


import sqlite3
from constantes import *
# import sql.constantes 
def conectar_db():
    conexion = sqlite3.connect(DATABASE_NAME)
    cursor = conexion.cursor()
    return conexion,cursor


conectar_db()

