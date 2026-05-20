'''Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
 la cuenta atrás desde ese número hasta cero separados por comas.'''

numero = input("Introduce un numero: ")
numero = int(numero)

lista = []

for i in range(numero, -1, -1):
    lista.append(i)

    

print(", ".join(str(n) for n in lista))