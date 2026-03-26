def eat_ghost(power_pallet_active, touching_ghoust):
	return power_pallet_active and touching_ghoust

def Score( touching_dot, power_pallet_active):
	return touching_dot or  power_pallet_active 

def lose (power_pallet_active, touching_ghoust):
	return  touching_ghoust and not power_pallet_active 

def win(eat_All_Pallet, touching_ghoust, power_pallet_active):
    return eat_All_Pallet and not (touching_ghoust and not power_pallet_active)

print("Tarea No. 1 - Definir si PacMac se come un fantasma")
print("Puedo Comerme el Fantasma:",eat_ghost(True, True))
print("Puedo Comerme el Fantasma:",eat_ghost(True, False))
print("Puedo Comerme el Fantasma:",eat_ghost(False, True))
print("Puedo Comerme el Fantasma:",eat_ghost(False, False))

print ()
print ()
print("Tarea No. 2 - Definir si PacMac anota puntos")

print("PacMac anota puntos:",Score(True, True))
print("PacMac anota puntos:",Score(True, False))
print("PacMac anota puntos:",Score(False, True))
print("PacMac anota puntos:",Score(False, False))

print ()
print ()
print("Tarea No. 3 - Definir si PacMac Pierde")

print("PacMac Pierde:",lose(True, True))
print("PacMac Pierde:",lose(True, False))
print("PacMac Pierde:",lose(False, True))
print("PacMac Pierde:",lose(False, False))

print ()
print ()
print("Tarea No. 4 - Definir si PacMac Gana")


print("PacMac Gana:",win(True, True, True))
print("PacMac Gana:",win(True, False, True))
print("PacMac Gana:",win(True, False, False))
print("PacMac Gana:",win(False, True, False))

