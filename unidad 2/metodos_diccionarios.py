# METODOS para trabajar con diccionarios

datos_personales = {
    "nombre" : "Ignacio",
    "edad" : 19,
    "titulo": "Ingenieria en Informatica"
     }

print("\n")
      
# El metodo KEYS() devuelve una lista con las claves del diccionario
claves = datos_personales.keys()
print(claves)

print("\n")

# El metodo VALUES() devuelve una lista con los valores del diccionario
valores = datos_personales.values()
print(valores)

print("\n")

#El metodo GET() permite obtener el VALOR de un elemento mediante su clave
nombre = datos_personales.get("nombre")
print(nombre)

print("\n")

# El metodo ITEMS() permite obtener cada uno de los pares de elementos
print(datos_personales.items())

print("\n")

# Para agregar un nuevo elemento al diccionario, se asigna un nuevo valor a una nueva clave
datos_personales["universidad"] = "Inacap"
print(datos_personales)

print("\n")

# El metodo POP() permite eliminar un elemento del diccionario, entregando la clave del elemento a eliminar
datos_personales.pop("titulo")
print(datos_personales)

# El metodo CLEAR() permite eliminar todos los elementos del diccionario, dejando el diccionario vacio
datos_personales.clear()
print(datos_personales) 