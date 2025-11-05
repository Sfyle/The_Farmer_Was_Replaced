from navigation import *

def plant_pumpkin():	
	goto(num_drones()-1,0)
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		if get_entity_type() != Entities.Pumpkin:
			plant(Entities.Pumpkin)
		if get_water() <= 0.8 and num_items(Items.Water) > get_world_size() ** 2: 
			use_item(Items.Water)
		move(North)

	can_recolt = False
	while can_recolt != True:
		for i in range(get_world_size()):
			if (get_entity_type() == Entities.Dead_Pumpkin) or (get_entity_type() == None):
				can_recolt = False
				plant(Entities.Pumpkin)
			move(North)
		can_recolt = True
