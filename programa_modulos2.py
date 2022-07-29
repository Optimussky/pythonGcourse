# Modulos parte 2

#import programa_modulos


#print(programa_modulos.saludar("Alberto"))
#user = programa_modulos.Usuario("Alberto", "optimussky@gmail.com")
#print(user.nombre)

# Si deseo importar un modulo de un archivo fuera de este directorio..
# from .. import my_module

from programa_modulos import Usuario

user = Usuario("Alberto", "optimussky@gmail.com")
print(user.nombre, user.email)

