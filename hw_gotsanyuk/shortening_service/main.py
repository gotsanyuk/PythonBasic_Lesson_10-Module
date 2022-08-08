import shelve


def add_link():
    'функція додавання зсилок та перевірки введених даних'
    files = shelve.open('data')
    next = 1  # _за допомогою цієї змінної запустимо приймання короткої зсилки, якщо посилання буде коректне
    while True:
        url = input('Введіть посилання: ')
        if len(url) <= 2:
            print('ERROR: Посилання повинне містити принаймні три символи\n')
            continue
        for link in files:  # _перевіряємо чи посилання вже існує
            if url in files[link]:
                print(f'Посилання вже існує, його коротка назва: {link}')
                next = 0

        while next == 1:  # _вводимо коротке посилання, і проходимо перевірки, чи не використовуєтсья і т.д.
            url_name = input('Введіть коротку назву посилання: ')
            if len(url_name) == 0:
                print('ERROR: Назва повинна містити хоча б один символ\n')
                continue
            elif url_name in files:
                print(f'ERROR: Назва "{url_name}" вже використовується\n')
                continue
            files[url_name] = url
            break
        files.close()  # _гарно закриваємо файл
        break


def show_link():
    files = shelve.open('data')
    'функція яка показує посилання по запиту його короткої назви'
    link_show = input('Введіть назву посилання: ')
    link = files.get(link_show)
    if link:
        print(link)
    else:
        print('ERROR_404: В списку такої назви не знайдено')
    files.close()
