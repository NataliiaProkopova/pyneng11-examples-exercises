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

config_dict = {'access': access_template, 'trunk':trunk_template}
input_dict = {'access': 'Введите номер VLAN: ', 'trunk': 'Введите разрешенные VLANы: '}

intf_type = input('Введите режим работы интерфейса (access/trunk): ')
intf_name = input('Введите тип и номер интерфейса: ')
vlans_list = input(input_dict[intf_type])

print(f'\ninterface {intf_name}')
out_config = '\n'.join(config_dict[intf_type])
print(out_config.format(vlans_list))