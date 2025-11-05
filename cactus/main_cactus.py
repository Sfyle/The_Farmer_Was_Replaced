from plant_cactus import *
from sort_cactus_x import *
from sort_cactus_y import *

clear()

while True:
	while (get_pos_x() != 0):
		move(West)
	while get_pos_y() != 0:
		move(South)

	drones = []
	for i in range(max_drones()):
		drone = spawn_drone(plant_cactus)
		drones.append(drone)
	drones.pop()
	
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		if get_entity_type() != Entities.Cactus:
			plant(Entities.Cactus)
		if get_water() <= 0.5 and num_items(Items.Water) > get_world_size() ** 2: 
			use_item(Items.Water)
		move(North)
		
	for drone in drones:
		if drone != None and has_finished(drone) == False:		
			wait_for(drone)
	
	drones = []
	for i in range(max_drones()):
		drone = spawn_drone(swap_cactus_x)
		drones.append(drone)
		drone = spawn_drone(swap_cactus_y)
		drones.append(drone)
	
	while (get_pos_x() != 0):
		move(West)
	while get_pos_y() != 0:
		move(South)
	
	for drone in drones:
		if drone != None and has_finished(drone) == False:		
			wait_for(drone)
	
	init_cactus = measure()
	move(West)
	move(South)
	end_cactus = measure()
	if end_cactus > init_cactus:
		harvest()
		#clear()
	move(East)
	move(North)
