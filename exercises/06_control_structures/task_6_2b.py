# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите IP адрес в формате 10.10.1.1: ")
ip_list = ip.split('.')
correct_ip = True

while correct_ip:
    ip_list = ip.split('.')
    if not len(ip_list) == 4:
        print("Неправильный IP-адрес")
        ip = input("Введите IP адрес в формате 10.10.1.1: ")
    else:
        for number in ip_list:
            if not (number.isdigit() and int(number) in range(256)):
                print("Неправильный IP-адрес")
                ip = input("Введите IP адрес в формате 10.10.1.1: ")
                break
        else:
            correct_ip = False
#if correct_ip == False:
#    print ("Неправильный IP-адрес")
if 0 < int(ip_list[0]) < 224:
    print("unicast")
elif 224 <= int(ip_list[0]) <= 239:
    print("multicast")
elif ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
else:
    print("unused")