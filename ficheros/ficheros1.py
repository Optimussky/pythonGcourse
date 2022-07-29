# Ficheros 1

#nombre = str(input("Ingrese su nombre: "))
#print(nombre)


def leer_fichero():
    # Abrir el archivo en modo lectura
    file = open('file.txt','r')

    dato = file.read()
    file.close()
    print(dato)

leer_fichero()


def escribir_fichero():
    # Abrir el archivo en modo escritura
    file = open('file.txt', 'w')
    dato = "Mi apellido es Romero\n"
    file.write(dato)
    file.close()

# Ejecutar funcion leer fichero
escribir_fichero()
#leer_fichero()


# Escribir en fichero anidando texto
file = open('file.txt','a')
dato = "Esta linea es nueva y se agrega si borrar nada"
file.write(dato)
file.close()
leer_fichero()


