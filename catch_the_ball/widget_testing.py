import tkinter # Подключаем графическую библиотеку
def button1_command(): #Обработчик нажатия кнопки button1
    print("button1 click")

def print_hello(event): # универсальный обработчик событий
    me=event.widget
    if me == button2:
        print("Hello, I'm button2")

root = tkinter.Tk() # Создаем главное окно
button1 = tkinter.Button(root, text="button1", command=button1_command) #создали кнопку button1 и задали обработчик ее нажатия
button1.pack() #автоматически разместили button1 в главном окне

button2 = tkinter.Button(root, text="button2") #создали кнопку button2
button2.pack() #автоматически разместили button2 в главном окне
button2.bind("<Button>",print_hello)

tkinter.mainloop() # Запускаем основной цикл программы
