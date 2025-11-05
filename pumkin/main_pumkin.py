from plant_pumpkin import *

clear()

while True:
	while (get_pos_x() != 0):
		move(West)
	while get_pos_y() != 0:
		move(South)

	drones = []
	for i in range(max_drones()):
		drone = spawn_drone(plant_pumpkin)
		drones.append(drone)
	drones.pop()
	
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
		
	for drone in drones:
		if drone != None and has_finished(drone) == False:		
			wait_for(drone)
	
	while (get_pos_x() != 0):
		move(West)
	while get_pos_y() != 0:
		move(South)
		
	init_pumpkin = measure()
	move(West)
	move(South)
	end_pumpkin = measure()
	if init_pumpkin == end_pumpkin:
		harvest()
		#clear()
	move(East)
	move(North)
