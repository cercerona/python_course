import tkinter
from random import choice, randint

canvas_width = 400
canvas_height = 300
timer_delay = 120 # определяет задержку в вызове таймера
gravitational_acceleration = 9.8 # Ускорение свободного падения
dt = 0.1 # квант физического времени

class MovingUnit:
    """Абстрактный класс, определяющий движущийся объект (шарик-мишень, шарик-пулю)
    Содержит атрибуты _x, _y, _Vx, _Vy, _R, _avatar
    и абстрактный (запрещенный к ввызову извне) метод fly()
    Наследниками являются классы шарика-мишени (Ball) и шарика-пули (Shell)"""

    def __init__(self, x, y, Vx, Vy, R, avatar):
        self._x  = x
        self._y = y
        self._Vx = Vx
        self._Vy = Vy
        self._R = R
        self._avatar = avatar
        self._deleted = False

    def fly(self):
        """Абстрактный метод fly()"""
        raise RuntimeError

    def delete(self):
        """
        Удаляет изображение объекта с холста
        :return: Ничего
        """
        if not self._deleted:
            canvas.delete(self._avatar)
            self._deleted = True


    def deleted(self):
        """
        :return: True, если объеект уже удален
        """
        return self._deleted


class Shell(MovingUnit):
    """
    Класс, определяющий объекты-пули
    Не отражается от стенок, уничтожается, если вылетает за пределы поля.
    Двигается по гравитационной траектории.
    """
    radius = 5
    maximal_number = 3
    color = 'black'
    def __init__(self, x, y, Vx, Vy):
        """

        """
        R = Shell.radius
        fill_color = Shell.color
        avatar = canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=fill_color, outline=fill_color)
        super().__init__(x, y, Vx, Vy, R, avatar)

    def fly(self):
        """
        Определяет гравитационную траекторию движения пули
        """
        ax = 0 # Проекция ускорения на ось X
        ay = gravitational_acceleration # Проекция ускорения на ось Y
        self._x += self._Vx*dt + ax*dt**2/2
        self._y += self._Vy*dt + ay*dt**2/2
        self._Vx += ax*dt
        self._Vy += ay*dt

        canvas.coords(self._avatar, self._x, self._y, self._x + 2*self._R, self._y + 2*self._R) # смещение координат

        #fixme: пока не отслеживается вылет за пределы поля, когда снаряд надо униичтожить

class Ball(MovingUnit):
    """
    Класс, определяющий шарики-мишени
    """
    initial_number = 20# число шариков для игры
    minimal_radius = 15
    maximal_radius = 40
    available_colors = ["green", "blue", "red"]
    minimal_Vx = -2# Минимальное значение скорости по оси X
    maximal_Vx = 2# Максимальное значение скорости по оси X
    minimal_Vy = -2# Минимальное значение скорости по оси Y
    maximal_Vy = 2 # Максимальное значение скорости по оси Y

    def __init__(self):
        """
        Создаем объект-шар в случайной позиции на холсте, закрашенный случайным цветом и
        со случайными значениями скоростей по осям X и Y
        """
        R = randint(Ball.minimal_radius, Ball.maximal_radius)
        x = randint(0+R, canvas_width-1-2*R)
        y = randint(0+R, canvas_height-1-2*R)
        Vx = randint(Ball.minimal_Vx, Ball.maximal_Vx)
        Vy = randint(Ball.minimal_Vy, Ball.maximal_Vy)

        fill_color = choice(Ball.available_colors)
        avatar = canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=fill_color,  outline=fill_color)


        super().__init__(x, y, Vx, Vy, R, avatar)

    def fly(self):
        """Отбиваемся от стены"""
        self._x = self._x + self._Vx
        self._y = self._y + self._Vy

        if self._x <= 0:
            self._x = 0
            self._Vx = -1*self._Vx
        elif self._x + 2*self._R >= canvas_width:
            self._x = canvas_width-2*self._R-1
            self._Vx = -1*self._Vx
        if self._y <= 0:
            self._y = 0
            self._Vy = -1*self._Vy
        elif self._y + 2*self._R >= canvas_height:
            self._y = canvas_height-2*self._R-1
            self._Vy = -1*self._Vy

        canvas.coords(self._avatar, self._x, self._y, self._x + 2*self._R, self._y + 2*self._R) # смещение координат


class Gun:# Класс, определяющий объект-пушку
    def __init__(self):
        self._x = 0# абсцисса начала пушки
        self._y = canvas_height-1# ордината начала пушки
        self._lx = 30# направление пушки по абсциссе
        self._ly = -30# направление пушки по ординате
        self._avatar = canvas.create_line(self._x, self._y, self._x+self._lx, self._y+self._ly)

    def shoot(self):
        """
        Метод, осуществляющий выстрел.
        :return Возвращает объект-пулю
        """
        shell = Shell(self._x + self._lx, self._y + self._ly, 2*self._lx, 2*self._ly)# Создаем объект-пулю
        return shell


def init_game():
    """
    Создает необходимое для игры число объектов-шариков и пушку
    :return: ничего
    """
    global balls, gun, shells_on_fly# Объявляем глобальный массив, который будет содержать объекты-шарики, пушку
    balls = [Ball() for i in range(Ball.initial_number)]
    gun = Gun()# создаем объект-пушку
    shells_on_fly = []# массив, содержащий пули

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
    canvas.grid(row = 1, column = 0, columnspan = 3)# упаковка холста
    scores_text.grid(row = 0, column = 2)# упаковка текстового поля
    canvas.bind('<Button-1>', click_event_handler)

def hitting(unit1, unit2):
    """
    Определяет пересекаются ли два графических объекта: объект пуля и объект шарик-мишень, т.е. есть ли попадание
    :param unit1: Объект пуля
    :param unit2: Объект шарик-мишень
    :return: True, если объекты пересекаются и False, если нет
    """
    if((unit1._x >= unit2._x) and (unit1._x <= (unit2._x+2*unit2._R)))\
            and ((unit1._y >= unit2._y) and (unit1._y <= (unit2._y+2*unit2._R)))\
            or ((unit1._x+2*unit1._R >= unit2._x) and ((unit1._x+2*unit1._R) <= (unit2._x+2*unit2._R)))\
            and (((unit1._y+2*unit1._R) >= unit2._y) and ((unit1._y+2*unit1._R) <= (unit2._y+2*unit2._R))):
        return True
    else:
        return False


def remove_deleted_units_from_list(units):
    """
    Удаляет элементы списка, изображения которых удалены с холста (у которых выставлен флаг _deleted
    :param units: Список, из которого необходимо удалить элементы
    :return: ничего
    """
    delta = 0 # Смещение в списке
    for i in range(len(units)):
        if units[i].deleted():
            delta +=1
        else:
            units[i-delta] = units[i]

    if delta != 0:
        units[:] = units[:-delta]


def timer_event():
    """Запускает таймер каждые timer_delay миллисекунд, определенных в глобальной переменной timer_delay.
    Двигает шарик и пулю, вызывая метод fly()"""
    for ball in balls:
        ball.fly()
    for shell in shells_on_fly:
        shell.fly()

    for ball in balls:
        for shell in shells_on_fly:
            if hitting(shell, ball):
                ball.delete()# Удаляем изображение мишени
                shell.delete()# Удаляем изображение пули

    remove_deleted_units_from_list(shells_on_fly)
    remove_deleted_units_from_list(balls)

    canvas.after(timer_delay, timer_event)

def click_event_handler(event):
    """
    Обрабатывает событие клика левой кнопкой мышки на холсте (выстрел)
    :return объект-пулю"""
    global shells_on_fly
    shells_on_fly.append(gun.shoot())


if __name__ == "__main__":
    init_main_window()
    init_game()
    timer_event()
    root.mainloop()
