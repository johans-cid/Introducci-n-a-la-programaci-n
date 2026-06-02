try:
    numero = int(input("Ingrese un numero entero positivo: "))
    factorial = 1
    if numero >= 0:
        for i in range(1, numero+1):
            factorial *= i
        print(factorial)
    else:
        print("Error: tu numero tiene que ser positivo")
except Exception as error:
    print(f"No se puede realizar la factorizacion por el siguiente error: {error}")