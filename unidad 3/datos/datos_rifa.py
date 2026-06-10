import os 
from datos import listado_rifas

def guardar_rifa(rifa):
    listado_rifas.append(rifa)
    try:
        ruta = os.path.join("unidad 3/datos/","listado_rifas.py")
        ruta_absoluta = os.path.abspath(ruta)
        ruta_real = os.path.realpath(ruta_absoluta)
        with open(ruta_real,"+w") as archivo:
            archivo.write("import datetime\n")
            archivo.write(f"listado_rifas ={listado_rifas}")
            archivo.close()
    except Exception as error:
        print(error)