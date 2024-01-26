persona1= str(input("primer jugador dijite una de las opciones pieda-papel-tijera"))
persona2= str(input("segundo jugador dijite una de las opciones pieda-papel-tijera"))

match persona1,persona2:
case "piedra","papel":
print ('gana papel primer jugador')

case "papel","piedra":
print ('gana papel segundo jugador')

case "tijera","papel":
print ('gana tijera gana el primer jugador')

case "papel","tijera":
print ('gana tijera gana el segundo jugador')

case "tijera","piedra":
print ('gana piedra gana el segundo jugador')

case "piedra","tijera":
print ('gana piedra gana el segundo jugador')