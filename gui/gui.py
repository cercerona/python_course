from tkinter import *

main_window = Tk()  # Создадим главное окно программы
main_window.title('Программа визуализации отчетов')  # Зададим заголовок главного окна программы

main_frame =  Frame(main_window)  # Создадим главный фрейм окна отчета
main_frame.config(bg='black')
main_frame.pack(side=TOP, expand=YES, fill=BOTH)  # Растянем фрейм на все пространство главного окна

top_frame = Frame(main_frame)  # Создадим фрейм для кнопки выбора файла-отчета
top_frame.config(bg='grey')
top_frame.pack(side=TOP, fill=X)  # Привяжем фрейм к верхней границе и будем растягивать по стороне X
open_file_button = Button(top_frame, text = 'Open report')
open_file_button.pack(side=RIGHT)  # Поместим справа кнопку открытия файла с отчетом
open_file_label = Label(top_frame, text = 'Report filename:')
open_file_label.pack(side=LEFT, expand=YES, fill=X)    # Поместим слева кнопку открытия файла с отчетом

table_frame = Frame(main_frame)  # Создадим фрейм для размещения таблицы с данными
table_frame.config(bg='grey')
table_frame.pack(side=LEFT, expand=YES, fill=BOTH)

canvas_frame = Frame(main_frame)  # Создадим фрейм для размещения графика
canvas_frame.config(bg='blue')
canvas_frame.pack(side=RIGHT, expand=YES, fill=BOTH)


if __name__ == "__main__":
    main_window.mainloop()
