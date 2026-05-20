'''Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''
print()
contraseña = input("Establesca su contraseña: ")

while True:
    print()
    ingreso = input("Ingrese su contraseña: ")
    if contraseña == ingreso:
        print("Contraseña correcta!")
        break
    else:
        print("Contraseña incorrecta, intentelo de nuevo.")
