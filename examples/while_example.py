'''
# Пример бесконечного цикла
while True:
    print('Type Ctrl-F2 to stop me!')
'''
'''
# Пример цикла - уменьшаем строку
x = 'Hello!'
while x != '':  # Пока x - не пустая строка
    print(x, end = ' ')
    x = x[1:]  # Вырезать первый символ из строки x
'''
'''
# Пример перебора значений в цикле
a = 0
b = 10

while a < b:
    print(a, end = ' ')
    a = a + 1
'''
'''
# Пример использования инструкции continue
x = 10
while x != 0:
    x = x - 1
    if x % 2 != 0: continue  # Нечетное? пропустить вывод
    print(x, end = ' ')
'''

# Пример использования инструкции break
while True:
    name = input('Введите Ваше имя: ')
    if name == 'stop': break
    print('Привет, ', name, '!' )
