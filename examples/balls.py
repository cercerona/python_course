import tkinter

canvas_color = "white"
canvas_width = 400
canvas_height = 300


def init_main_window():
    """Создает и инициализирует виджеты главного окна"""
    global root, canvas  # глобальные виджеты гл.окна и холста
    root = tkinter.Tk()  # создали главное окно
    root.title("Поймай шарик")  # задали заголовок главного окна
    canvas = tkinter.Canvas(root, background=canvas_color,\
                            width=canvas_width, height=canvas_height)
    canvas.pack()
    canvas.bind('<Button>', click_ball)
    canvas.bind('<Motion>', move_all_balls)


if __name__ == "__main__":
    init_main_window()  # Инициализация главного окна
    root.mainloop()
