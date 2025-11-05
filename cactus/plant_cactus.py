from navigation import *

def plant_cactus():
	goto(num_drones()-1,0)
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		if get_entity_type() != Entities.Cactus:
			plant(Entities.Cactus)
		if get_water() <= 0.5 and num_items(Items.Water) > get_world_size() ** 2: 
			use_item(Items.Water)
		move(North)
		
