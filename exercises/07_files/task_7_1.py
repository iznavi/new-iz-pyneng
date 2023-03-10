# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

template = '''
Prefix                {ip}
AD/Metric             {metric}
Next-Hop              {hop}
Last update           {time}
Outbound Interface    {intf}
'''
with open('ospf.txt', 'r') as f:
    for line in f:
        line_list = line.split()
        ip = line_list[1]
        metric = line_list[2].strip('[]')
        hop = line_list[4].rstrip(',')
        time = line_list[5].rstrip(',')
        intf = line_list[-1]
        print(template.format(ip=ip, metric=metric, hop=hop, time=time, intf=intf))