# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    """
    Функция возвращающая словарь портов в режиме access или trunk
    """
    access = {}
    trunk = {}
    
    with open(config_filename, "r") as f:
        for line in f:
            if line.startswith("interface"):
                intf = line.split()[-1]
            elif "access vlan" in line:
                vlan = line.split()[-1]
                #vlan_int = [int(vl) for vl in line.split()[-1]]
                access[intf] = int(vlan)
            elif  "allowed vlan" in line:
                trunk[intf] = [int(vl) for vl in line.split()[-1].split(',')]
        mode = access, trunk
    return mode

print(get_int_vlan_map("config_sw1.txt"))