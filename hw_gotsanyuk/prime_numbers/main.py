def simple_numbers(ending):
    '''Створюю функцію генератора'''
    for x in range(2, ending): #_перебираємо числа
        p = True
        for d in range(2, int(x ** 0.5) + 1):
            if x % d == 0:
                p = False
        if p == True:
            yield x



def give_numbers(end):
    'функція яка ітерує генератор по числах'
    for y in simple_numbers(end): #_вказуємо до якого числа виводити прості числа
        print(y)



end = 10
