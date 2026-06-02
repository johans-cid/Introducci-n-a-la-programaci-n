try:
    numero = int(input("Ingrese un numero entero cualquiera: "))
    if numero > 0:
        print("Su numero es positivo")
    elif numero < 0:
        print("Su numero es negativo")
    else:
        print("Su numero es cero")
except Exception as error:
    print(f"No se puede realizar la factorizacion por el siguiente error: {error}")