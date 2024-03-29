# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress


def convert_ranges_to_ip_list(ip_list):
    """
    Функция конвертирует список IP-адресов в разных форматах в список,
    где каждый IP-адрес указан отдельно.
    """
    add_ips = []
    for ip in ip_list:
        if "-" in ip:
            cur_ip = ip.split("-")
            start_ip = cur_ip[0]
            try:
                ipaddress.ip_address(cur_ip[1])
                add_ips.append(start_ip)
                new_ip = ipaddress.ip_address(start_ip)
                for i in range(int(start_ip.split(".")[3]), int(cur_ip[1].split(".")[3])):
                    new_ip += 1
                    add_ips.append(str(new_ip))
                print(add_ips)
            except ValueError:
                end_octet = int(cur_ip[1])
                add_ips.append(start_ip)
                new_ip = ipaddress.ip_address(start_ip)
                for i in range(int(start_ip.split(".")[3]), end_octet):
                    new_ip += 1
                    add_ips.append(str(new_ip))
                print(add_ips)
        else:
            add_ips.append(ip)
    return add_ips
            

if __name__ == "__main__":
    some_ip = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    convert_ranges_to_ip_list(some_ip)