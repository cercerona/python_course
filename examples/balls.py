import tkinter
from random import choice, randint

canvas_color = "white"
canvas_width = 400
canvas_height = 300

ball_initial_number = 20  # Число шариков для игры
ball_minimal_radius = 15  # Минимальный радиус шарика
ball_maximal_radius = 40  # Максимальный радиус шарика
ball_available_colors = ['green', 'blue', 'red', '#FF00FF', '#FFFF00']

def random_color():
    """Возвращает случайное значение цвета"""
    return choice(ball_available_colors)

def create_random_ball():
    """Создает шарик, закрашенный случайным цветом"""
    R = randint(ball_minimal_radius, ball_maximal_radius)
    x = randint(0+R, canvas_width-1-2*R)
    y = randint(0 + R, canvas_height - 1 - 2 * R)
    canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=random_color())

def click_ball(event):
    """Обработчик нажатия левой кнопки мышки"""
    print('x = ' + str(event.x) + ', ' + 'y = ' + str(event.y))

def move_all_balls(event):
    """Сдвигает шарики"""
    pass  # fixme

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

def init_catch_ball_game():
    pass  #fixme

if __name__ == "__main__":
    init_main_window()  # Инициализация главного окна
    init_catch_ball_game()
    root.mainloop()
