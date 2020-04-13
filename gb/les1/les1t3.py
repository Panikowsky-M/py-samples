print('Вводите данные в анкету')

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = int(input('Введите возраст: '))
weight = int(input('Введите вес: '))

med_info = name + ' ' + surname + ', ' + str(age) + \
           ' возраст,' + 'вес' + str(weight)

good = 'Вы здоровы'
hosp = 'Необходима запись к врачу'
bad = 'Вы больны необходима госпитализация!'


if weight >= 50 and weight <= 120:
    if age < 30:
        print(med_info + ' - ' + good )
    elif age >= 40:
        print(med_info + ' - ' + good ) 
    else:
        print(med_info + ' - ' + good )
else:
    if age < 30:
        print(med_info + ' - ' + bad)
    elif age >= 40:
        print(med_info + ' - ' + hosp)
    else:
        print(med_info + ' - ' + bad)
