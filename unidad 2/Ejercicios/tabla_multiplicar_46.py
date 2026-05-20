'''Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.'''

for i in range(1, 11):
    print()
    print(f"Tabla del {i}")
    for n in range(1,11):
        print(f"{i} X {n} = {i*n}")