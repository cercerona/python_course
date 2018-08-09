import tkinter

def click_ball(event):
    """Обработчик событий мышки на игровом холсте
    :param event: событие с координатами клика
    :return: ничего
    """
    print(event.x, event.y)

def create_random_ball():
    canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=random_color())

def init_main_window():
    """Создает и инициирует виджеты окна игры"""
    global root, canvas #создание глобальных виджетов главного окна и холста
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, background='white', width=400, height=400)
    canvas.bind("<Motion>", click_ball)
    canvas.pack()

if __name__ == "__main__":
    init_main_window()
    root.mainloop()
