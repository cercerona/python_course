def question_6():
    a1 = input('Введите a1: ')
    a2 = input('Введите a2: ')
    b1 = input('Введите b1: ')
    b2 = input('Введите b2: ')
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)
    a1 = a1*b2 + b1*a2
    a2 = a2*b2
    print('Результат a1/a2 = %d/%d'%(a1, a2))

def question_7():
    x = int(input('Введите значение x: '))
    y = x*x
    y = y*y
    y = 5 * y
    a = x*x
    a = 1 - a
    y = y + a
    y = y*y
    print('y = %d'%y)

if __name__ == "__main__":
    question_7()