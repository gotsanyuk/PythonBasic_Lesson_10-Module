from .main import add_link, show_link


def main_menu_2():
    'головне меню'
    while True:
        print('- МЕНЮ -2-')
        n = int(input('[1] - Показати посилання \n[2] - Додати силку \n[3] - Вихід\n -> '))
        if n == 1:
            show_link()
        elif n == 2:
            add_link()
        elif n == 3:
            return False
        else:
            print('ERROR: Я не розумію вас, виберіть від 1 до 3 із пунктів меню:')
            continue
