
import tkinter as tk

win = tk.Tk()
win.geometry('600x300')
win.title('Drawing Application')

# Create canvas with white background
canvas = tk.Canvas(win, bg="white", highlightthickness=0)
canvas.pack(fill=tk.BOTH, expand=True)

# Brush size and color variables
brush_size = 4
brush_color = "black"

def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size / 2, y - brush_size / 2, x + brush_size / 2, y + brush_size / 2),
                       fill=brush_color, width=0)

def change_color(new_color):
    global brush_color
    brush_color = new_color

# Create color palette buttons
colors = ["black", "red", "blue", "green", "yellow","orange"]
for i, color in enumerate(colors):
    button = tk.Button(win, text=color, bg=color, command=lambda c=color: change_color(c))
    button.place(x=10 + i * 30, y=10)

# Add an eraser button
eraser_button = tk.Button(win, text="Eraser", command=lambda: change_color("white"))
eraser_button.place(x=10 + len(colors) * 30, y=10)

canvas.bind('<B1-Motion>', draw_on_canvas)

win.mainloop()
