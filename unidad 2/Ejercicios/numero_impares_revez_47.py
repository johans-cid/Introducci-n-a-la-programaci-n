'''Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1'''

numero = int(input("Ingrese un numero: "))

impares = []

for i in range(1, numero+1):
    if i % 2 != 0:
        impares.append(i)

coma = []
contador = 0
for n in impares:
    fila = impares[contador::-1]
    print(" ".join(str(x) for x in fila))
    contador += 1



