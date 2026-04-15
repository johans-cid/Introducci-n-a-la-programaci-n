# Metodos para modificar cadenas de texto

nombre_completo_miniscula = "ignacio cid"
nombre_completo_mayuscula = "IGNACIO CID"
lorem_ipsum = """Lorem ipsum dolor sit amet consectetur
 adipisicing elit.
 Voluptas, voluptate."""
rut = "22311551-9"

#print (dir(nombre_completo))
print(nombre_completo_miniscula)
print(nombre_completo_mayuscula)

# El metodo CAPITALIZE() deja en mayuscula la primera letra del texto
print(nombre_completo_miniscula.capitalize())
#print(lorem_ipsum.capitalize())

# El metodo LOWER() deja en minuscula todo el texto
print(nombre_completo_mayuscula.lower())

# El metodo UPPER() deja en mayuscula todo el texto
print(nombre_completo_miniscula.upper())

# El metodo TITLE() deja en mayuscula la primera letra de cada palabra del texto
print(nombre_completo_miniscula.title())
#print(lorem_ipsum.title())

# El metodo LEN (length, largo = tamaño) devuelve la cantidad de caracteres que tiene el texto, incluyendo espacios
print(len(nombre_completo_miniscula))
print(len(lorem_ipsum))

# El metodo SPLIT permite cortar una cadena de caracteres en el caracter indicado
# Si no se entrega ningun argumento al metodo split, el metodo SPLIT cortara la cadena en cada espacio
nombre_split = nombre_completo_miniscula.split()
print(nombre_split)

# Si se entrega un argumento al metodo SPLIT, el metodo SPLIT cortara la cadena en cada caracter indicado
nombre_split = nombre_completo_miniscula.split("i")
print(nombre_split)

rut_split  = rut.split("-")
print(rut_split)