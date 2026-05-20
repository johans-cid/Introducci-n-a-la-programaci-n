def crear_diccionario():
    campos = {
        "id" : "",
        "tarea" : "",
        "prioridad" : "",
        "estado" : ""
    }
    
    
    return campos

def pedir_datos():
    tarea_ingresar = input("Ingrese su tarea:")
    prioridad_ingresar = input("Ingrese la prioridad de la tarea:")

    return tarea_ingresar, prioridad_ingresar

def agregar_diccionario():
    tarea_usuario, prioridad_usuario = pedir_datos()
    datos = crear_diccionario()
    
    new_tarea = datos.update({"tarea": tarea_usuario})
    new_prioridad = datos.update({"prioridad": prioridad_usuario})
    
    print(datos)
    return new_tarea, new_prioridad

def guardar_diccionarios(a):
    lista = []  
    return lista

while True:
    print("""Que quieres hacer:

[1] Agregar una tarea  
[2] Ver tareas
[3] Estado de tarea
[4] Eliminar tarea
          
          
          """)
    decision = int(input(""))
    if decision == 1:
        agregar_diccionario()
        
    
    
        




    
    
    

    
    





    


