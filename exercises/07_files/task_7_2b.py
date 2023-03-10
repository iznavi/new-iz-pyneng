# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

ignore = ["duplex", "alias", "configuration"]

src = argv[1]
dst = argv[2]
#file_name = 'config_sw1.txt'
count = 0

with open(src, 'r') as s, open(dst, 'w') as d:
    for line in s:
        if not line.startswith('!'):
            for word in ignore:
                if word in line:
                    count += 1
                    break
                else:
                    count = 0
            if count == 0:
                d.write(line)