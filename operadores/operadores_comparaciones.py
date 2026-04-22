# Operadores de comparación
# permiten evaluar si los valores son equivalentes o distintos

igual = 5 == 10/2
distinto = 5 != 6
mayor_que = 5 > 4
menor_que = 5 < 4
mayor_igual_que = 5 >= 4
menor_igual_que = 5 <= 4

print(f"5 == 10/2: {igual}")
print(f"5 != 6: {distinto}")
print(f"5 > 4: {mayor_que}")
print(f"5 < 4: {menor_que}")
print(f"5 >= 4: {mayor_igual_que}")
print(f"5 <= 4: {menor_igual_que}")

contrasena = "pepito"
contrasena_usurario = input("Ingrese su contraseña: ")

if contrasena == contrasena_usurario:
    print("Contraseña correcta, bienvenido")
    print(contrasena == contrasena_usurario)

