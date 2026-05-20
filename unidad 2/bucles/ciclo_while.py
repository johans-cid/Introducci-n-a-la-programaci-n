contador = 0
while contador < 10:
    print(contador)
    contador = contador + 1

print("Ciclo While mientras el contador < 10")

contrasena = "papas"
intento = 0
while intento < 3:
    contrasena_usuario = input("Ingrese su contraseña")
    if contrasena == contrasena_usuario:
        print("Su contraseña es correcta")
    else:
        if intento < 3:
            print("Su contraseña es incorrecta, intentelo de nuevo")
        else:
            print("Contraseña incorrecta, cerrando sistema")
    intento += 1