import tkinter as tk

def draw_map(the_map, window):

    for label in window.children.copy():
        window.children[label].destroy()

    for line in the_map:
        label = tk.Label(window, text=line)
        label.pack()
