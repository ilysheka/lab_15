import os
from re import sub, UNICODE

def cons_manager(n = '=' * 100):
    '''
    Функция получает номер функции и передает его в основную
    '''
    print('Bас приветствует файловый менеджер. Выберите одну из следующих функций:\n'
          '1. Создание файла\n2. Удаление файла\n3. Чтение текста из файла\n4. Изменение файла\n'
          f'5. Поиск файлов по части названия, расширению, дате, размеру\n0. Выход из программы\n{n}')
    number = input(f'Введите номер функции: ')
    return number

def create_file(n = '=' * 100):
    '''
    Функция получает название файла в переменную file_name,
    затем создаёт файл с названием file_name. 
    Пробелы заменяются на _ , а также удаляются ненужные знаки(реализовано с помощью регулярных выражений).
    После выполнения возвращает в основную функцию.
    '''
    file_name = input(f'{n}\nВы выбрали создание файла(1). Если нужно вернуться назад, введите 0.\nВведите название файла с расширением: ')
    if file_name == str(0):
        main()
    else:
        file_name = sub(r'[^\w\s.]', '', file_name.replace(' ', '_'), flags=UNICODE)
        with open(file_name, 'w'):
            print(f'Файл {file_name} создан.')
        print(f'{n}\nСоздание файла произошло успешно. Возвращаемся в начало.\n{n}')
        main()

def delete_file(n = '=' * 100):
    '''
    Функция получает название файла в переменную file_name,
    затем удаляет файл с названием file_name. 
    Пробелы заменяются на _ , а также удаляются ненужные знаки(реализовано с помощью регулярных выражений).
    После выполнения возвращает в основную функцию.
    '''
    file_name = input(
        f'{n}\nВы выбрали удаление файла(2). Если нужно вернуться назад, введите 0.\nВведите название файла с расширением: ')
    if file_name == str(0):
        main()
    else:
        file_name = sub(r'[^\w\s.]', '', file_name.replace(' ', '_'), flags=UNICODE)
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f'Файл {file_name} удалён.')
        else:
            print(f'Файл {file_name} не найден.')
        print(f'{n}\nУдаление файла произошло успешно. Возвращаемся в начало.\n{n}')
        main()

def read_file(n = '=' * 100):
    file_name = input(
        f'{n}\nВы выбрали чтение текста из файла(3). Если нужно вернуться назад, введите 0.\nВведите название файла с расширением: ')
    if file_name == str(0):
        main()
    else:
        file_name = sub(r'[^\w\s.]', '', file_name.replace(' ', '_'), flags=UNICODE)
        with open(file_name, 'r', encoding='UTF-8') as file:
            for i in file.readlines():
                print(i)
        print(f'{n}\nПрочтение файла произошло успешно. Возвращаемся в начало.\n{n}')
        main()

def change_file(n = '=' * 100):

    def simple_read_file(file_name:str, n): # Функция выводит содержимое файла
        print(n)
        m = 0
        with open(file_name, 'r', encoding='UTF-8') as file:
            print(f'Название файла: {file_name}\nСодержимое:')
            for i in file.readlines():
                m += 1
                print(f'{m}: {i}')
        print(n)

    def add_str(file_name:str): # Функция добавляет введённую строку
        num_str = int(input('Вы выбрали добавление строки в файл(1).\nВведите номер строки, после которой будет вставлена ваша: '))
        sobst_str = input('Введите строку: ')
        with open(file_name, 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            lines.insert(num_str, sobst_str + '\n')
        with open(file_name, 'w', encoding='UTF-8') as file:
            file.writelines(lines)
        print('Строка вставлена успешно. Возвращаемся в начало.')
        main()

    def remove_str(file_name:str): # Функция удаляет указанную строку
        num_str = int(input('Вы выбрали удаление строки из файла(2).\nВведите номер строки, которая будет удалена: '))
        with open(file_name, 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            lines = lines[:num_str - 1] + lines[num_str:]
        with open(file_name, 'w', encoding='UTF-8') as file:
            file.writelines(lines)

    functions = {'default':simple_read_file,
                 '1':add_str,
                 '2':remove_str}

    file_name = input(
        f'{n}\nВы выбрали изменение файла(4).\nВведите название файла с расширением: ')
    functions['default'](file_name, n)
    num_func = input(f'Что конкретно вам нужно? Выберите:\n1. Добавить строку в файл.\n2. Удалить строку из файла.\n0. Вернуться.\n')
    if  num_func == str(0):
        main()
    elif num_func in functions:
        functions[num_func](file_name)
        print(f'{n}\nИзменение файла произошло успешно. Возвращаемся в начало.\n{n}')
        main()
    else:
        print('Неизвестная команда. Повторим: ')
        change_file()

def find_file(n = '=' * 100): 
    import datetime

    print(f'{n}\nВы выбрали поиск файлов по части названия, расширению, дате, размеру(5)')
    results = []
    name_part = input("Часть названия (Enter - file): ").strip().lower().replace(' ', '_')
    name_part = name_part if name_part != '' else 'file'
    extension = input("Расширение (Enter - txt): ").strip().lower() 
    extension = '.' + extension if extension != '' else '.txt'
    # name_cat = input("Название папки, директории (Enter - текущая): ").strip().lower().replace(' ', '_')
    # name_cat = name_cat if name_cat != '' else '.'
    name_cat = '.'
    size_min = input("Минимальный размер в байтах (Enter - 0): ")
    size_min = float(size_min) if size_min != '' else float(0)
    size_max = input("Максимальный размер в байтах (Enter - максимально возможное число): ")
    size_max = float(size_max) if size_max != '' else float(99 ** 99)
    date_days = input("Файлы изменённые за последние N дней (Enter - минимально возможное N): ").strip()
    date_days = int(date_days) if date_days != '' else 0
    for i in os.listdir(name_cat):
        size_file = os.path.getsize(i)
        last_change_date = os.path.getmtime(i) # В переменную передаётся дата последнего изменения файла
        # а точнее количество секунд, прошедших с 1 января 1970 года
        last_change_date = datetime.datetime.fromtimestamp(last_change_date) # Переводим секунды в дату
        date_now = datetime.datetime.now()
        need_time = date_now - datetime.timedelta(date_days)
        if name_part in i and extension in i[-6:] and size_min <= size_file <= size_max and need_time >= last_change_date:
            results.append(i)
    if len(results) >= 1:
        print(f'Найденные файлы:', end=' ')
        for i in results:
            end = ', '
            if i == results[-1]:
                end = '\n'
            print(i, end=end)
        print('Возвращаемся в начало: ')
        main()
    else:
        print('Файлы не найдены. Повторим: ')
        find_file()

def break_func():
    print('До новых встреч!')

def main():
    number_func = cons_manager()
    funcs = {'1':create_file,
            '2':delete_file,
            '3':read_file,
            '4':change_file,
            '5':find_file,
            '0':break_func}
    if number_func in funcs:
        funcs[number_func]()
    else:
        print(f'Неизвестная команда. Повторим:')
        main()
main()