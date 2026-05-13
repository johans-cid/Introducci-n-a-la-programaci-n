# Establecer las variables para los precios
ps3_game = 20
ps4_game = 45

#Preguntar la cantidad de cada juego que se comprará
num_ps3_games = int(input("¿Cuantos juegos para ps3?"))
num_ps4_games = int(input("¿Cuantos juegos para ps4?"))


#Calcular el total de cada tipo de juego

ps3_total = num_ps3_games * ps3_game
ps4_total = num_ps4_games * ps4_game
#Calcular el precio total
total_cost = ps3_total + ps4_total

#Imprimir el precio total del pedido
print(f"El precio de tu pedido es:${total_cost}")