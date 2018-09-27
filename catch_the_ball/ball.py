import tkinter
from random import choice, randint

canvas_width = 400
canvas_height = 300
canvas_color = "white"
ball_initial_number = 20 #Число шариков для игры
ball_minimal_radius = 15
ball_maximal_radius = 40
ball_available_colors = ["green", "blue", "red", "#FF00FF", "#FFFF00"]

def click_ball(event):
    """Обработчик событий мышки на игровом холсте
    :param event: событие с координатами клика
    По клику мышки необходимо удалять объект, над которым пришелся клик и засчитывать пользователю
    необходимое колличество очков.
    :return: ничего
    """
    obj = canvas.find_closest(event.x, event.y)
    print(canvas.coords(obj))
    x1, y1, x2, y2 = canvas.coords(obj)
    if (x1 <= event.x <= x2) and (y1 <= event.y <= y2):
        canvas.delete(obj)
        #fixme: учесть в очках
        #create_random_ball()

def move_all_balls(event):
    """
    Передвигает все шарики на чуть-чуть
    :param event:
    :return: нет
    """
    for obj in canvas.find_all():
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        canvas.move(obj, dx, dy)


def random_color():
    """Возвращает случайное значение цвета
    :param: нет
    :return: цвет
    """
    return choice(ball_available_colors)


def init_catch_ball_game():
    """
    Создает необходимое для игры число шариков.
    :return:
    """
    for i in range(ball_initial_number):
        create_random_ball()


def create_random_ball():
    """Создает шарик, закрашенный случайным цветом
    :param ничего
    :return: ничего
    """
    R = randint(ball_minimal_radius, ball_maximal_radius)
    x = randint(0+R, canvas_width-1-2*R)
    y = randint(0+R, canvas_height-1-2*R)
    canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=random_color())


def init_main_window():
    """Создает и инициирует виджеты окна игры
    :param: нет
    :return: ничего
    """
    global root, canvas #создание глобальных виджетов главного окна и холста
    root = tkinter.Tk()
    root.title("Поймай шарик")
    canvas = tkinter.Canvas(root, background = canvas_color, width=canvas_width, height=canvas_height)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()


if __name__ == "__main__":
    init_main_window()
    init_catch_ball_game()
    root.mainloop()
