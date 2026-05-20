#Listas => List
#Es una coleccion ORDENADA Y MUTABLE de datos de cualquier tipo

print("\nListas en python")
mi_primera_lista = ["gato", 50, True]
print(type(mi_primera_lista))
print(mi_primera_lista)

print("El primer elemento de la lista es:{} y el segundo es {}".format(mi_primera_lista[0], mi_primera_lista[1]))
nombre_personal = input("Ingrese su nombre: ")
mi_primera_lista[0] = nombre_personal
print(mi_primera_lista)

#Diccionarios => Dict
#Es una coleccion ORDENADA Y MUTABLE de pares de datos de cualquier tipo
#Los datos de un diccionario ocupan el doble de esapcio en memoria

print("\nDiccionarios en python")
mi_primer_diccionario = {"nombre" : "Ignacio cid" , "edad" : 19 , "asistio clase hoy?" : True}
print(type(mi_primer_diccionario))
print(mi_primer_diccionario)
print("El primer dato del diccionario es: {}".format(mi_primer_diccionario["nombre"]))

# CONJUNTOS => Set
# Es una coleccion NO ORDENADA e INMUTABLE de datos de cualquier tipo 


print("\nConjuntos")
mi_primer_conjunto = {50, "gato", True}
print(type(mi_primer_conjunto)) 
print(mi_primer_conjunto)
mi_primer_conjunto.add(25)

#Tuplas => Tuple
# Es una coleccion ORDENADA e INMUTABLE de datos de cualquier tipo

print("\nTuplas en python")
mi_primera_tupla = ("gato", 50, True)
print(type(mi_primera_tupla))
print(mi_primera_tupla)
print(mi_primera_tupla[0])

#La TUPLA no permite asignar un nuevo valor para los elementos, la siguiente asignacion es invalida:
#nombre_personal = input("Ingrese su nombre: ")
#mi_primera_tupla[0] = nombre_personal 
#print(mi_primera_tupla[0])

