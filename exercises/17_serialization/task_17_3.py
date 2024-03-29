# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re
import csv
from pprint import pprint



def parse_sh_cdp_neighbors(sh_cdp_str):
    
    regex = re.compile(r"(?P<dev>\S+) +(?P<lint>\S+ \d\S+)(?: +\S+){5} +(?P<port>\S+ \d\S+)")
    
    result = {}
    
    match_iter = re.finditer(regex, sh_cdp_str)
    device = re.search(r"(\S+)>", sh_cdp_str).group(1)
    result[device] = {}
    for match in match_iter:
        intf = {}
        intf[match.group('dev')] = match.group('port')
        result[device][match.group('lint')] = intf
    return result
    
    
if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        file = f.read()
        pprint(parse_sh_cdp_neighbors(file))
        
    