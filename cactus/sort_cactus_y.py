def swap_cactus_y():
	row = num_drones()
	for i in range(row):
		move(East)
		move(East)
	
	has_swapped = True
	
	while has_swapped == True:
		has_swapped = False	
		for i in range(get_world_size()):
			# Swap lines for achievement
      # if get_pos_y() != get_world_size() -1 and measure(North) > measure():
      if get_pos_y() != get_world_size() -1 and measure(North) < measure():
				swap(North)
				has_swapped = True
			move(North)
		move(East)
		for i in range(get_world_size()):
			# Swap lines for achievement
      # if get_pos_y() != get_world_size() -1 and measure(North) > measure():
			if get_pos_y() != get_world_size() -1 and measure(North) < measure():
				swap(North)
				has_swapped = True
			move(North)
		move(East)
		for i in range(get_world_size()):
			# Swap lines for achievement
      # if get_pos_y() != get_world_size() -1 and measure(North) > measure():
			if get_pos_y() != get_world_size() -1 and measure(North) < measure():
				swap(North)
				has_swapped = True
			move(North)
		move(East)
		for i in range(get_world_size()):
			# Swap lines for achievement
      # if get_pos_y() != get_world_size() -1 and measure(North) > measure():
			if get_pos_y() != get_world_size() -1 and measure(North) < measure():
				swap(North)
				has_swapped = True
			move(North)
		move(West)
		move(West)
		move(West)
