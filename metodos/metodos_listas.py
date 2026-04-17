lista_compras = ["pan", "leche", "huevos", "frutas", "verduras"]
lista_animales = ["gato", "perro", "conejo", "hamster", "pez"]
lista_numeros = [1, 445, 6, 86, -7]

print(lista_animales)
print(type(lista_animales))

# El metodo LEN (length, largo = tamaño) devuelve la cantidad de elementos que tiene la lista

print(len(lista_animales))

print("\n")

nuevo_animal = input("Ingrese un nuevo animal: ")
lista_animales.append(nuevo_animal)
print(len(lista_animales))
print(lista_animales)

print("\n")

# El metodo INSERT permite agregar un elemento en un lugar (indice) especifico de la lista

otro_animal = input("Ingrese otro animal: ")
lista_animales.insert(2, otro_animal)
print(len(lista_animales))
print(lista_animales)

print("\n")

# El metodo EXTEND permite agregar los elementos de una lista a una lista
# Agregamos una lista ya creada, uniendo ambas listas
lista_animales.extend(lista_compras)
print(len(lista_animales))
print(lista_animales)

print("\n")

# agregamos una lista manualmente
lista_animales.extend(["tortuga", "serpiente"])
print(len(lista_animales))
print(lista_animales)

print("\n")

#El metodo POP permite eliminar un elementos de una lista
#Si al metodo POP no se le entrega un indice, el metodo POP eliminara el ultimo elemento de la lista
lista_animales.pop()
print(len(lista_animales))
print(lista_animales)

#Si al metodo POP se le entrega un indice, el metodo POP eliminara el elemento del indice entregado
lista_animales.pop(2)
print(len(lista_animales))
print(lista_animales)

#Si al metodo POP se le  indico el argumento -1, el metodo POP eliminara el ultimo elemento de la lista
lista_animales.pop(-1)
print(len(lista_animales))
print(lista_animales)

print("\n")

# El metodo REMOVE elimina un elemento por su valor
lista_animales.remove("perro")
print(len(lista_animales))
print(lista_animales)

print("\n")

# El metodo CLEAR elimina todos los elementos de la lista, dejando la lista vacia
lista_animales.clear()
print(len(lista_animales))
print(lista_animales)

print("\n")

# El metodo SORT ordena los elementos de la lista de menor a mayor, o alfabeticamente
lista_compras.sort()
print(len(lista_compras))
print(lista_compras)

print("\n")

# El metodo REVERSE ordena los elementos de la lista de mayor a menor, o alfabeticamente al reves
lista_compras.reverse()
print(len(lista_compras))
print(lista_compras)

print("\n")

# El metodo SORT ordena los elementos de la lista de menor a mayor, o alfabeticamente
lista_numeros.sort()
print(len(lista_numeros))
print(lista_numeros)

print("\n")

# El metodo REVERSE ordena los elementos de la lista de mayor a menor, o alfabeticamente al reves
lista_numeros.reverse()
print(len(lista_numeros))
print(lista_numeros)

print("\n")
