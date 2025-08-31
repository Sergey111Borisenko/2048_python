import move_up
import move_down
import move_left
import move_right
import draw_map

import random
import tkinter as tk

a_number = random.randint(1, 2) * 2
b_number = random.randint(1, 2) * 2
a_position = random.randint(0, 15)
b_position = random.randint(0, 15)

while a_position == b_position:
    b_position = random.randint(0, 15)

the_map = [[0, 0, 0, 0], 
           [0, 0, 0, 0], 
           [0, 0, 0, 0],
           [0, 0, 0, 0]]

x = a_position % 4
y = (a_position - a_position % 4) // 4
the_map[y][x] = a_number

x = b_position % 4
y = (b_position - b_position % 4) // 4
the_map[y][x] = b_number

# avant le début de la partie


window = tk.Tk()

key = ""
can_move = True
while key != "exit" and key != "quit" and can_move == True:
    print(str(the_map).replace(", [", ",\n ["))
    draw_map.draw_map(the_map, window)
    
    # window.mainloop()
    key = input()
    if key == "z":
        can_move = move_up.move_up(the_map)
    if key == "s":
        can_move = move_down.move_down(the_map)
    if key == "q":
        can_move = move_left.move_left(the_map)
    if key == "d":
        can_move = move_right.move_right(the_map)

print("Game Over")
