# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess
import platform

def ping_ip_addresses(ip_list):
    """
    Функция ожидает как аргумент список IP-адресов.

    Функция должна возвращать кортеж с двумя списками:
        * список доступных IP-адресов
        * список недоступных IP-адресов
    """
    pingable = []
    unpingable = []
    for ip in ip_list:
        if platform.system().lower() == "windows":
            reply = subprocess.run(['ping', '-n', '3', ip],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   encoding='utf-8')
        else:
            reply = subprocess.run(['ping', '-c', '3', ip],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   encoding='utf-8')
        
        if reply.returncode == 0:
            pingable.append(ip)
        else:
            unpingable.append(ip)
    print(f"Pingable: {pingable}, Unpingable: {unpingable}")
    return pingable, unpingable

if __name__ == "__main__":
    some_ip = ['8.8.8.8', '8.8.4.4', '192.32.21.1', '1.1.1.1']
    ping_ip_addresses(some_ip)