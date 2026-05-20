import math
# Resuelva los siguientes ejercicios mediante funciones,
# las que serán llamadas dentro de un menú de opciones.

# 1.- Cree una función que entregue el saludo "Buen día!"
def saludo_cordial():
    saludo = "Buen día!"
    return saludo

# 2.- Cree una función que solicite el nombre y el género al usuario y luego, 
# llamando a la función anterior, salude al usuario, el saludo debe quedar así: 
# "Buen día nombre_usuario!", 
# y agregue el texto "Hoy te ves hermosa" si el usuario es mujer 
# o "cómo estás campeón?" si el usuario es hombre

def solicitar_datos():
    while True:
        print()
        print("Ingrese todo en minusculas.")
        print()
        nombre = input("Ingrese su nombre: ")
        genero = input("Ingrese su genero[hombre o mujer]: ")
        
        if genero == "hombre":
            print()
            print(f"Buen dia {nombre}, como estas campeon?")
            print()
            
            break
        elif genero == "mujer":
            print()
            print(f"Buen dia {nombre}, Hoy te ves hermosa")
            print()
            break
        else:
            print()
            print("Error: algun dato escrito es incorrecto, intentelo de nuevo.")
            print()



# 3.- Cree una función que permita calcular el área de una circunferencia 
# y otra que permita calcular el volumen de un cilindro usando la función anterior
# los datos deben ser ingresados por el usuario

def area_circulo(a): 
    area = math.pi * (a*a)
    
    return area 

def area_cilindro(a,b):
    area = a * b
    return area

# 4.- Cree una función que pida un número entero al usuario 
# y calcule el factorial de ese número

def factorial(a):
    
    factorial = math.factorial(a)
    return factorial 
# 5.- Solicite al usuario el ingreso del nombre del estudiante, 
# luego solicite el ingreso de las notas del estudiante y calcule el promedio 
# y mostrar su situacion final, Aprobado (nota>=4.0) y Reprobrado (nota < 4.0)
# 
# la salida del programa debe ser el siguiente
# Nombre: nombre_estudiante
# Notas: notas
# Promedio: promedio
# Situacion Final: Aprobado/Desaprobado

def calcular_promedio():
    print()
    nombre_estudiante = input("Ingrese su nombre: ")
    print("IMPORTANTE: rango de notas[1-7]")
    ingreso_notas = []
    while True:
        try:
            print()
            notas = input("Ingrese sus notas [-1 Salir]: ")
            
            if notas == "-1":               
                break
            elif notas != "" and notas >= "1.0" and notas <= "7.0":
                notas = float(notas)
                ingreso_notas.append(notas)  
                print(ingreso_notas)   
            else:
                print()
                print("Dato no valido! Intentelo nuevamente")
        except ValueError as e:
            print()
            print("Error: Ingrese solo numeros")
        
        
    
    suma = 0
    for numero in ingreso_notas: 
        suma = suma + numero
    
    promedio = suma / len(ingreso_notas)
    situacion_final = 0
    if promedio >= 4.0:
        situacion_final = "Aprobado"
        
    elif promedio < 4.0:
        situacion_final = "Desaprobado"
    
    print()
    print("=================")
    print(f"Nombre: {nombre_estudiante}")
    print(f"Notas: {ingreso_notas}")
    print(f"Promedio: {promedio}")
    print(f"Situacion final: {situacion_final}")
    print("=================")
        
    
    
    


def menu_principal():
    opciones_menu = {
        
                "1":"Saludo",
                "2":"Nombre y genero usuario",
                "3":"Volumen de un cilindro",
                "4":"Calcular factorial",
                "5":"Promedio",
                "0":"Salir"}
                
    while True:    
        print()
        for clave,valor in opciones_menu.items():
            print(f"[{clave}] {valor}")
            
        
        seleccion = input(f"seleccione su opcion [0-{len(opciones_menu) - 1}]: ")
        opciones_validas = ["0","1","2","3","4","5"]
        
        if  seleccion in opciones_validas:
            if seleccion != "0":
                if seleccion == "1":
                    respuesta = saludo_cordial()
                    print(respuesta)       
                elif seleccion == "2": 
                    solicitar_datos()
                elif seleccion == "3":
                    radio = float(input("radio: "))
                    imprimir_circulo = area_circulo(radio)
                    print(f"El area de tu circulo es de: {imprimir_circulo}")
                    
                    altura = float(input("Ingrese la altura de su cilindro: "))
                    imprimir_cilindro = area_cilindro(imprimir_circulo, altura)
                    print(f"El volumen de tu cilindro en es de:{imprimir_cilindro}")
                elif seleccion == "4": 
                    numero = int(input("ingrese numero: "))
                    imprimir_factorial = factorial(numero)
                    print(f"El factorial de {numero} es {imprimir_factorial}")
                elif seleccion == "5":
                    calcular_promedio()
            else:
                break


menu_principal()