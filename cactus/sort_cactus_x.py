def swap_cactus_x():
	row = num_drones()
	for i in range(row):
		move(North)
		move(North)
	
	has_swapped = True
	
	while has_swapped == True:
		has_swapped = False	
		for i in range(get_world_size()):
      # Swap lines for achievement
      # if get_pos_x() != get_world_size() -1 and measure(East) < measure():
			if get_pos_x() != get_world_size() -1 and measure(East) < measure():
				swap(East)
				has_swapped = True
			move(East)
		move(North)
		for i in range(get_world_size()):
      # Swap lines for achievement
      # if get_pos_x() != get_world_size() -1 and measure(East) < measure():
			if get_pos_x() != get_world_size() -1 and measure(East) < measure():
				swap(East)
				has_swapped = True
			move(East)
		move(North)
		for i in range(get_world_size()):
      # Swap lines for achievement
      # if get_pos_x() != get_world_size() -1 and measure(East) < measure():
			if get_pos_x() != get_world_size() -1 and measure(East) < measure():
				swap(East)
				has_swapped = True
			move(East)
		move(North)
		for i in range(get_world_size()):
      # Swap lines for achievement
      # if get_pos_x() != get_world_size() -1 and measure(East) < measure():
			if get_pos_x() != get_world_size() -1 and measure(East) < measure():
				swap(East)
				has_swapped = True
			move(East)
		move(South)
		move(South)
		move(South)
