lista_juegos = ["Dota 2","CS2","Plantas vs zombies","expedition 33"]
lista_numeros = [1,2,5,6,8]

for elemtento in lista_juegos:
    print(elemtento)

print()

print(f"\nRecorriendo la lista de numeros = {lista_numeros}")
for numero in lista_numeros:
    resultado = numero * numero
    print(f"{numero} X {numero} = {resultado}")

print()

conjunto_animales = {"perro","gato","lombris","ñandu"}
for animales in conjunto_animales:
    print(animales) 

print()

tupla_datos_personales = ("wendy",25,"bolibiana","espectador")
for dato in tupla_datos_personales:
    print(dato)

print()

diccionarios_asignaturas = {
    "codigo":"TI3011",
    "nombre":"introduccion a la programacion",
    "seccion":"IEI-N1-C2",
    "Alumnos":20

}
for elemento in diccionarios_asignaturas:
    print(elemento)

print()

for elemento in diccionarios_asignaturas.items():
    clave = elemento[0]
    valor = elemento[1]
    print(f"clave: {clave} - valor: {valor}")