import subprocess
import ipaddress

def start_ip():
    while True:
        try:
            start = input("Введите начальный IP-адрес (например, 192.168.1.1): ").strip()
            # Проверяем, что это правильный IP-адрес
            ipaddress.IPv4Address(start)
            break
        except ipaddress.AddressValueError:
            print("Ошибка: Неправильный формат IP-адреса. Попробуйте снова.")
    return ipaddress.IPv4Address(start)

def end_ip():
    while True:
        try:
            end = input("Введите конечный IP-адрес (например, 192.168.1.1): ").strip()
            # Проверяем, что это правильный IP-адрес
            ipaddress.IPv4Address(end)
            break
        except ipaddress.AddressValueError:
            print("Ошибка: Неправильный формат IP-адреса. Попробуйте снова.")
    return ipaddress.IPv4Address(end)

def check_alive(ip_address):
    try:
        result = subprocess.run(['ping', '-n', '1', '-w', '1000', ip_address], 
                        capture_output=True, timeout=2)
        #subprocess.run вызывает утилиту ping в командной строке, -n - количество, 1 - 1 пинг запрос, -w 1000 - 1 секунда на запрос
        #timeout - общее выполнение команды, capture_output - сохраняет вывод в result

        #для Linux:
        
        # result = subprocess.run(['ping', '-c', '1', '-W', '1', ip_address],
        #                 capture_output=True, timeout=2)
        return result.returncode == 0
    except:
        return False

def generate_list_ip(start, end):
    if start > end:
        print('Ошибка: начальный IP должен быть меньше или равен конечному')
        return []
    ip_list = []
    while start <= end:
        ip_list.append(str(start))
        start += 1
    return ip_list

def main():
    start = start_ip()
    end = end_ip()
    list_ip = generate_list_ip(start, end)
    result = []
    for i in list_ip:
        if check_alive(i):
            print(f'IP-адрес {i} доступен.')
            result.append(i)
        else:
            print(f'IP-адрес {i} недоступен.')
    print(f'Список доступных в сети IP-адресов: ')
    for n in result:
        print(n)

main()