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

# Пример перебора значений в цикле
a = 0
b = 10

while a < b:
    print(a, ' ')
    a = a + 1

