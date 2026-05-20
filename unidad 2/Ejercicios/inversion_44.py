'''Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
 y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.'''

dinero_invertir = input("Cual es la cantidad de dinero que desea invertir?: ")
dinero_invertir = float(dinero_invertir)
interes_anual = input("Cual es el interes anual?: ")
interes_anual = float(interes_anual)
anos_totales = input("Cual es la cantidad de anos que invertira el dinero?: ")
anos_totales = int(anos_totales)

anos = []
for i in range(1, anos_totales + 1):
    anos.append(i)

for i in anos:
    dinero_invertir = dinero_invertir + (dinero_invertir * (interes_anual/100))
    print(f"año {i}: {dinero_invertir:.2f}")
    


