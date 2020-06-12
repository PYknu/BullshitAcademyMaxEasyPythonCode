datab = {}
print('Welcome to my easiest database')
while True:
    print('Что ты хочешь сделать?')
    print('Введи P чтобы [P]ut, G чтобы [G]et или L чтобы показать [L]ist')
    print('Или введи Q чтобы [Q]uit')
    action = input()
    if action == 'P':
        k = input('Введите ключ: ')
        d = input('Введите данные: ')
        datab[k] = d
    elif action == 'G':
        k = input('Введите ключ: ')
        if not k in datab:
            print('Такого ключа к сожалению нет в базе данных')
        else:
            print('Ваши данные при этом ключе: %s' % datab[k])
    elif action == 'L':
        print('В базе данных хранится: ')
        print(datab)
    elif action == 'Q':
        print('Пока, друг!')
        break
