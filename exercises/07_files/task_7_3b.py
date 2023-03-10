# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
user_vlan = input('Введите номер VLAN: ')

data = list()
with open('CAM_table.txt', 'r') as f:
    for line in f:
        if '.' in line:
            l = line.split()
            vlan, mac, _, intf = l
            data.append([int(vlan), mac, intf])
    data.sort()
    for vlan, mac, intf in data:
        if vlan == int(user_vlan):
            print(f'{vlan:<10}{mac:20}{intf}')