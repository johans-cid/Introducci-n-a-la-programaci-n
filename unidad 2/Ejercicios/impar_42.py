'''Escribir un programa que pida al usuario un número entero positivo
 y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas. '''

numero = input("Introduce un numero: ")
numero = int(numero)

lista = []

for i in range(1, numero + 1):
    lista.append(i)

a = 1
impares = []
for i in lista:
    if i == a:
        impares.append(i)
        a+=2
print(", ".join(str(n) for n in impares))