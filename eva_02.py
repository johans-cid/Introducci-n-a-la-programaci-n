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
        


def menu_principal():
    while True:    
            print()
            print("=======================")
            print("SELECCIONE UN EJERCICIO")
            print("=======================")
            print("""
==========
[1] Saludo
[2] Nombre y genero usuario
[3] Volumen de un cilindro
[4] Calcular factorial
[5] Salir    
==========        """)
            seleccion = input("Eleccion: ")
            
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
                break

menu_principal()