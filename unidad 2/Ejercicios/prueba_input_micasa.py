nombre = input("¿Cuál es tu nombre? ")
saludo = "Hola, buen dia "  
print("{} es un nombre bonito".format(nombre))

#CONCATENACION de candenas de texto
print(saludo + nombre)

str_edad = input("¿Cuántos años tienes? ")
edad_entero = int(str_edad)
edad_flotante = float(str_edad)
print(type(edad_entero))
print(type(edad_flotante))
print(edad_flotante)
print("Tienes {} años, Disfruta tus {} años".format(edad_entero, edad_entero))

numero_uno = 25
numero_dos = 30
#La operacion + con dos numeros, opera aritmeticamente, sumandolos y entregando un resultado numerico
print(numero_uno + numero_dos)
#La operacion + con dos cadenas de texto, las concatena, es decir, las une y entrega una nueva cadena de texto
print(saludo + str_edad)
#La operacion + con una cadena de texto y 
# un numero, no se puede realizar, ya que son tipos de datos diferentes, por lo que se produce un error
# print(str_edad + numero_uno)

nombre = input("Ingrese su nombre ")
edad = input("Ingrese su edad ")

print("Hola, {} buen dia, tienes {} años".format(nombre, edad))