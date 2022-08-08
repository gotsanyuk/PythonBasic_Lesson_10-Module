from .main import add_link, show_link #_імпортуємо доступ до функцій додавання та показ зсилок


def main_menu_1():
    'головне меню'
    while True:
        print('- МЕНЮ -1-')
        n = int(input('[1] - Додати силку \n[2] - Показати посилання \n[3] - Вихід\n -> '))
        if n == 1:
            add_link()
        elif n == 2:
            show_link()
        elif n == 3:
            return False
        else:
            print('ERROR: Я не розумію вас, виберіть від 1 до 3 із пунктів меню:')
            continue
