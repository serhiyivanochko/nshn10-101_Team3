from tkinter import *
window = Tk()


def create_board():
    count_rows = 8
    width = 75
    start_x = 0
    start_y = 0
    cell_color = "white"
    for i in range(count_rows):
        for j in range(count_rows):
            canvas.create_rectangle(start_x, start_y, start_x + width, start_y + width, fill=cell_color)
            start_x = start_x + width
            if cell_color == "white":
                cell_color = "black"
            else:
                cell_color = "white"
        start_x = 0
        start_y = start_y + width
        if cell_color == "white":
            cell_color = "black"
        else:
            cell_color = "white"


canvas = Canvas(window, width=600, height=600)
canvas.pack()

create_board()

window.mainloop()