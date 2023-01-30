# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

mode = input("Введите режим работы интерфейса (access/trunk): ")

vlans_mode = {
    'access': 'Введите номер VLAN: ',
    'trunk': 'Введите разрешенные VLANы: '
}

interface = input("Введите тип и номер интерфейса: ")
vlan = input(vlans_mode[mode])

access_str = '\n'.join(access_template)
trunk_str = '\n'.join(trunk_template)

switchport_dic = {
    'access': access_str,
    'trunk': trunk_str
}

print(f"interface {interface}")
print(switchport_dic[mode].format(vlan))