'''Escribir un programa que pregunte al usuario su edad y muestre por 
pantalla todos los años que ha cumplido (desde 1 hasta su edad).'''

edad = input("cual es tu edad: ")
edad = int(edad)

numero = []
for i in range(1,edad+1):
    numero.append(i)

print(", ".join(str(n) for n in numero ))
