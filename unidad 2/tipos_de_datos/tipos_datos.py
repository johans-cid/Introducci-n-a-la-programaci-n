# Tipos de datos en Python

#Con el # se pueden escribir comentarios en el código, es decir,
#texto que no se ejecuta pero sirve para explicar o documentar el código.   

variable_texto = "Buen dia queridos estudiantes"
variable_entero = 25
variable_decimal = 3.14
variable_booleano = True

#Tipo de dato STRING str
print(variable_texto)
#Tipo de dato INTEGER int
print(variable_entero)
#Tipo de dato FLOATING float
print(variable_decimal)
#Tipo de dato BOOLEANO bool
print(variable_booleano)

print(type(variable_texto))
print(type(variable_entero))
print(type(variable_decimal))
print(type(variable_booleano))

#print(dir(variable_texto)) esto dice los metodos
print(variable_texto.split())
print(variable_texto.title())
print(variable_texto.upper())
print(variable_texto.islower())
print(variable_texto.split())

#print(dir(variable_entero)) esto dice los metodos
print(variable_entero.is_integer())
print(variable_decimal.is_integer())