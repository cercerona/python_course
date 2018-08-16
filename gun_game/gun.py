import tkinter
from random import choice, randint

canvas_width = 400
canvas_height = 300

class Ball:
    initial_number = 20#число шариков для игры
    minimal_radius = 15
    maximal_radius = 40
    available_colors = ["green", "blue", "red"]
    minimal_Vx = -2#Минимальное значение скорости по оси X
    maximal_Vx = 2#Максимальное значение скорости по оси X
    minimal_Vy = -2#Минимальное значение скорости по оси Y
    maximal_Vy = 2 #Максимальное значение скорости по оси Y

    def __init__(self):
        """
        Создаем объект-шар в случайной позиции на холсте, закрашенный случайным цветом и
        со случайными значениями скоростей по осям X и Y
        """
        R = randint(Ball.minimal_radius, Ball.maximal_radius)
        x = randint(0+R, canvas_width-1-2*R)
        y = randint(0+R, canvas_width-1-2*R)
        fill_color = choice(Ball.available_colors)
        self._R = R
        self._x = x
        self._y = y
        self._avatar = canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=fill_color)
        self._Vx = randint(Ball.minimal_Vx, Ball.maximal_Vx)
        self._Vy = randint(Ball.minimal_Vy, Ball.maximal_Vy)


def init_game():
    """
    Создает необходимое для игры число объектов-шариков и пушку
    :return: ничего
    """
    global balls# Объявляем глобальный массив, который будет содержать объекты-шарики
    balls = [Ball() for i in range(Ball.initial_number)]
    #FIXME надо еще создать пушку

def init_main_window():
    """Создает и инициирует виджеты окна игры
    :param: нет
    :return: ничего
    """
    global root, canvas, scores_value, scores_text  #создание глобальных виджетов главного окна и холста
    root = tkinter.Tk()
    root.title("Пушка")
    scores_value = tkinter.IntVar()
    canvas = tkinter.Canvas(root, background='white', width=canvas_width, height=canvas_height)
    scores_text = tkinter.Entry(root, textvariable = scores_value)
    canvas.pack()
    scores_text.pack()


if __name__ == "__main__":
    init_main_window()
    init_game()
    root.mainloop()
