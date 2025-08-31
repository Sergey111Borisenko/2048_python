import random

def is_the_map_filled(the_map):
    for line in the_map:
        for cell in line:
            if cell == 0:
                return False
    return True

def spawn_random_number(the_map):
    cell_number = random.randint(1, 2) * 2
    cell_x = random.randint(0, 3)
    cell_y = random.randint(0, 3)

    if the_map[cell_x][cell_y] == 0:
        the_map[cell_x][cell_y] = cell_number
    else:
        while the_map[cell_x][cell_y] > 0:
            cell_x = random.randint(0, 3)
            cell_y = random.randint(0, 3)
        the_map[cell_x][cell_y] = cell_number