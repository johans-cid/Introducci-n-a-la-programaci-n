print("\nSumando 2 numeros con metodo 'suma'")
def suma(a,b):
    try:
        resultado = a + b
        print(f"{a} + {b} = {resultado}")
    except Exception as error:
        print(f"No se puede realizar la operacion por el siguiente error: {error}")

print("\nSumando 2 numeros con metodo 'resta'")
def resta(a,b):
    try:
        resultado = a - b
        print(f"{a} - {b} = {resultado}")
    except Exception as error:
        print(f"No se puede realizar la operacion por el siguiente error: {error}")

print("\nSumando 2 numeros con metodo 'multiplicacion'")
def multiplicacion(a,b):
    try:
        resultado = a * b
        print(f"{a} * {b} = {resultado}")
    except Exception as error:
        print(f"No se puede realizar la operacion por el siguiente error: {error}")

print("\nSumando 2 numeros con metodo 'division'")
def division(a,b):
    try:
        resultado = a / b
        print(f"{a} / {b} = {resultado}")
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    except Exception as error:
        print(f"No se puede realizar la division por el siguiente error: {error}")

def convetir_a_float(valor):
    try:
        num_decimal = float(valor)
        return num_decimal
    except ValueError:
        print("No se puede convertir el valor a decimal.")
    except Exception as error:
        print(f"No se puede realizar la conversion por el siguiente error: {error}")
def solicitar_datos():
    numero1 = convetir_a_float(input("Ingrese el primer numero: "))
    numero2 = convetir_a_float(input("Ingrese el segundo numero: "))
    return(numero1,numero2)

ciclo = True
while ciclo == True:
    print("\nCalculadora en python")
    print("=====================")
    print("[1] Suma\n[2] Resta\n[3] Multiplicacion\n[4] Division\n[0] Salir")
    print("=====================")
    opcion = input("\nSeleccione una opcion[0-4]: ")

    if opcion == "0":
        print("\nGracias por usar la calculadora, vuelva pronto.")
        ciclo = False
    elif opcion == "1":
        num1, num2 = solicitar_datos()
        suma(num1, num2)
    elif opcion == "2":
        resta()
    elif opcion == "3":
        multiplicacion()
    elif opcion == "4":
        division()