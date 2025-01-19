import tkinter as tk
def draw_airplane(canvas):
    # Стены дома
    canvas.create_rectangle(100, 200, 300, 400, fill='lightyellow', outline='black')
    # Крыша
    canvas.create_polygon(80, 200, 200, 100, 320, 200, fill='brown', outline='black')
    # Окна
    canvas.create_rectangle(130, 250, 180, 300, fill='lightblue', outline='black')  # левое окно
    canvas.create_rectangle(220, 250, 270, 300, fill='lightblue', outline='black')  # правое окно
    # Дверь
    canvas.create_rectangle(180, 330, 220, 400, fill='saddlebrown', outline='black')
    canvas.create_oval(200, 360, 180, 375, fill='black')
    # Дымоход
    canvas.create_rectangle(230, 130, 260, 200, fill='gray', outline='black')  # дымоход
def main():
    root = tk.Tk()
    root.title("Рисование самолета")
    canvas = tk.Canvas(root, width=800, height=700, bg='white')
    canvas.pack()
    draw_airplane(canvas)
    root.mainloop()

main()
