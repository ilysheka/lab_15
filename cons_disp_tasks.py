import subprocess as sp

def cons_manager(n = '=' * 100):
    '''
    Функция получает номер функции и передает его в основную
    '''
    print('Bас приветствует файловый менеджер. Выберите одну из следующих функций:\n'
          '1. Вывод текущих процессов\n2. Запуск нового процесса\n3. Завершение процесса\n'
          f'0. Выход из программы\n{n}')
    number = input(f'Введите номер функции: ').strip()
    return number

def output_now_process():
    print('Вы выбрали вывод текущих процессов(1).')
    res = sp.run('tasklist', capture_output=True, text=True, check=True) # Для Windows
    # res = sp.run(['ps', 'aux'], capture_output=True, text=True, check=True) # Для Linux
    print(f'Запущенные процессы:\n{res.stdout}')
    print('Возвращаемся в начало.')
    main()

def start_new_process():
    dict_process = {
        '1':'notepad.exe',
        '2':'calc.exe',
        '4':'mspaint.exe'
    }
    inp = input(f'Вы выбрали запуск нового процесса(2). Выберите из перечня и напишите цифру,\nлибо процесс(например cmd.exe):\n'
                f'1. Блокнот.\n2. Калькулятор.\n3. Paint.\n0. Вернуться.\nВы выбираете: ').strip()
    if inp == '0':
        main()
    elif inp in dict_process:
        sp.Popen([dict_process[inp]])
        print(f'Запуск процесса {inp} произошёл успешно! Возвращаемся в начало.')
        main()
    else:
        try:
            sp.Popen([inp])
        except:
            print('Неизвестный процесс. Повторим:')
            start_new_process()
        else:
            print(f'Запуск процесса {inp} произошёл успешно! Возвращаемся в начало.')
            main()

def kill_process():
    inp = input('Вы выбрали завершение процесса(3). Введите процесс, или 0 чтобы вернуться: ').strip()
    if inp == '0':
        main()
    else:
        try:
            sp.run(['taskkill', '/F', '/PID', inp], check=True)
        except:
            print(f'Завершить процесс {inp} не удалось. Повторим:')
            kill_process()
        else:
            print(f'Процесс {inp} завершён. Возвращаемся в начало.')
            main()

def break_func():
    print('До новых встреч!')

def main():
    number_func = cons_manager()
    funcs = {
            '0':break_func,
            '1':output_now_process,
            '2':start_new_process,
            '3':kill_process}
    if number_func in funcs:
        funcs[number_func]()
    else:
        print(f'Неизвестная команда. Повторим:')
        main()
main()