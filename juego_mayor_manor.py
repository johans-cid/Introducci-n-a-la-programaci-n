import random

usuario = input("Ingrese su nombre de usuario:")

print()

print("=================================================")
print(f"Hola {usuario}, Bienvenido a 'Adivina el numero'")
print("=================================================")

print()

print("=======")
print("REGLAS")
print("=======")
print("""Adivina el número entre 1 y 100
Tienes intentos ilimitados
Te diré si es mayor o menor""")
print("=======")
print()



def pedir_numero():
    ciclo = True
    while ciclo == True:
        try: 
                numero = int(input("Ingrese su numero:"))
                if 100 >= numero >= 1:
                    ciclo = False 
                    return numero            
                else:
                    print(f"El numero {numero} no esta dentro del rango permitido.")
        except ValueError as e:
            print(f"Ingrese un caracter valido, codigo error:{e}")
    

intentos = 0


while True:
    if intentos == 0:
        numero_secreto = random.randint(1,100)
        
    numero = pedir_numero()
    intentos+=1
    print(f"Cantidad de intentos hasta ahora: {intentos}")
    if numero == numero_secreto:
        print()
        print("FELICITACIONES HAS ACERTADO")
        print(f"Tu cantidad de intentos TOTAL fue de: {intentos}")
        print()
        break
    elif numero > numero_secreto:
        print("EL NUMERO ES MENOR")
        
    else:
        print("EL NUMERO ES MAYOR")
        
    
    