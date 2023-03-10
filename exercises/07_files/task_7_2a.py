# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]

file_name = argv[1]
#file_name = 'config_sw1.txt'
count = 0

with open(file_name) as f:
    for line in f:
        if not line.startswith('!'):
            for word in ignore:
                if word in line:
                    count += 1
                    break
                else:
                    count = 0
            if count == 0:
                print(line.rstrip())