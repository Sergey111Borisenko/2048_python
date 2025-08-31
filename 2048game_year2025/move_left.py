import game2048

def move_left(the_map):
    i = 0
    j = 0
    while i < len(the_map):
        while j < len(the_map[0]) - 1:
            if the_map[i][j] == the_map[i][j + 1] and the_map[i][j] > 0:
                the_map[i][j] = the_map[i][j] * 2
                the_map[i][j + 1] = 0
                i = -1
                j = len(the_map[0])
            elif the_map[i][j] == 0 and the_map[i][j + 1] > 0:
                the_map[i][j] = the_map[i][j + 1]
                the_map[i][j + 1] = 0
                i = -1
                j = len(the_map[0])
            j = j + 1
        j = 0
        i = i + 1


    if game2048.is_the_map_filled(the_map) == True:
        return False
    game2048.spawn_random_number(the_map)
    return True
