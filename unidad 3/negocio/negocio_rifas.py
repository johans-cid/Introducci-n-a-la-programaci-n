from datos import listado_rifas
from prettytable import PrettyTable
from datos import guardar_rifa

def obtener_listado_rifas():
    tabla_rifas = PrettyTable()
    tabla_rifas.field_names = ["N°",'Nombre','Fecha Creación','Precio Número','Cantidad Rifas','Fecha Lanzamiento']

    for rifa in listado_rifas:
        tabla_rifas.add_row([rifa["n"],rifa['nombre'], rifa['fecha_creacion'], f'${rifa['precio']}', rifa['cantidad_rifas'], rifa['fecha_lanzamiento']])
    
    return tabla_rifas

def numero_rifa():
    if True:
        num = len(listado_rifas)+1
        return num
    


def crear_nueva_rifa(n,nombre, precio, cantidad_rifas, numeros_rifa, fecha_creacion, fecha_lanzamiento, premios):
    nueva_rifa = {
        "n":n,
        'nombre':nombre,
        'precio':precio,
        'cantidad_rifas':cantidad_rifas,
        'numeros_rifa':numeros_rifa,
        'fecha_creacion':fecha_creacion,
        'fecha_lanzamiento':fecha_lanzamiento,
        'premios':premios
        
    }
    guardar_rifa(nueva_rifa)



    