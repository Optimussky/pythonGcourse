#Manejo de errores en python



try:
    menu = int(input("Ingrese una opcion valida: "))
    print(f"Ha ingresado la opcion {menu}")
except ValueError as error:
    print(f"No se puede ingresar ese tipo de dato, error: {error}")


