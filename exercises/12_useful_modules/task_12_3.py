# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate


def print_ip_table(rchbl, unrchbl):
    """
    Функция отображает таблицу доступных
    и недоступных IP-адресов.
    """
    rchbl_key = ["Reachable"]
    unrchbl_key = ["Unreachable"]
    
    rchbl_dict = dict.fromkeys(rchbl_key, rchbl)
    rchbl_dict.update(dict.fromkeys(unrchbl_key, unrchbl))
    
    print(tabulate(rchbl_dict, headers='keys'))


if __name__ == "__main__":
    first = ['10.1.1.1', '10.1.1.2']
    second = ['10.1.1.7', '10.1.1.8', '10.1.1.9']
    print_ip_table(first, second)