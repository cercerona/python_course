import tkinter

def init_main_window():
    """Создает и инициирует виджеты окна игры"""
    global root, canvas #создание глобальных виджетов главного окна и холста
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, back)
