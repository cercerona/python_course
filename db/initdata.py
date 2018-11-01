#  Инициализировать данные для последующего сохранения в файлах
#  Записи
petr = {'name': 'Petr Petrov', 'age': 14, 'class': '8', 'letter': 'a', 'interest': 'chess'}
elen = {'name': 'Elen Sidorova', 'age': 14, 'class': '8', 'letter': 'a', 'interest': 'cooking'}
ivan = {'name': 'Ivan Ivanov', 'age': 13, 'class': '8', 'letter': 'b', 'interest': 'football'}
kate = {'name': 'Kate Sokolova', 'age': 14, 'class': '8', 'letter': 'b', 'interest': 'cooking'}

#  база данных
db = {}
db['petr'] = petr
db['elen'] = elen
db['ivan'] = ivan
db['kate'] = kate

if __name__ == "__main__":
    for key in db:
        print(key, '=>\n', db[key])
