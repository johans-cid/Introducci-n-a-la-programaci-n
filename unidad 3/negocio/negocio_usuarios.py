from datos import listado_usuarios
from prettytable import PrettyTable

def obtener_listado_usuarios():
    tabla_usuarios = PrettyTable()
    tabla_usuarios.field_names = ["Nombre","Apellido","Fecha de nacimiento","Direccion", "Tipo de usuario"]

    for usuario in listado_usuarios:
        tabla_usuarios.add_row([usuario["nombre"], usuario["apellido"], usuario["fecha nacimiento"], usuario["direccion"], usuario["tipo_usuario"]])

    return tabla_usuarios