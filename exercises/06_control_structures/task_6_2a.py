# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите IP адрес в формате 10.10.1.1: ")

ip_list = ip.split('.')
correct_ip = True

if not ip.count('.') == 3:
    correct_ip = False
else:
    for number in ip_list:
        if not (number.isdigit() and int(number) in range(256)):
            correct_ip = False       
            break
if correct_ip == False:
    print ("Неправильный IP-адрес")
elif 0 < int(ip_list[0]) < 224:
    print("unicast")
elif 224 <= int(ip_list[0]) <= 239:
    print("multicast")
elif ip == "255.255.255.255":
    print("local broadcast")
elif ip == "0.0.0.0":
    print("unassigned")
else:
    print("unused")
