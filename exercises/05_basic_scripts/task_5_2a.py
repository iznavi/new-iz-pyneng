# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

net = input("Введите IP-сеть в формате 10.0.0.0/24: ")

ip = net[0:net.find("/"):].split('.')
ip_bin = f"{int(ip[0]):08b}{int(ip[1]):08b}{int(ip[2]):08b}{int(ip[3]):08b}"
mask = net[net.find("/")+1::]
mask_bin = "1" * int(mask) + "0" * (32-int(mask))
listmask = [mask_bin[0:8], mask_bin[8:16], mask_bin[16:24], mask_bin[24:32]]
net_bin = ip_bin[0:int(mask):] + "0" * (32-int(mask))
net_list = [net_bin[0:8], net_bin[8:16], net_bin[16:24], net_bin[24:32]]

output_ip = """
Network:
{0:<10d}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
"""

output_net = """
Mask:
/{maskf}
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
"""

print(output_ip.format(int(net_list[0],2), int(net_list[1],2), int(net_list[2],2), int(net_list[3],2)))
print(output_net.format(int(listmask[0],2), int(listmask[1],2), int(listmask[2],2), int(listmask[3],2), maskf=mask))