# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map (config_filename):
    '''
    Функция обрабатывает конфигурационный файл коммутатора и возвращает кортеж из двух словарей
    config_filename - имя конфигурационного файла
    '''
    access_ports = {}
    trunk_ports = {}
    with open(config_filename, 'r') as f:
        for line in f:
            if line.startswith('interface'):
                intf = line.split()[-1]
                current_vlans = None
            if line.startswith(' switchport access'):
                current_vlans = int(line.split()[-1])
                access_ports[intf] = current_vlans
            if line.startswith(' switchport trunk allowed'):
                current_vlans = [int(vlan) for vlan in line.split()[-1].split(',')]
                trunk_ports[intf] = current_vlans
            if line.startswith(' duplex auto') and (not current_vlans):
                access_ports[intf] = 1

    return (access_ports, trunk_ports)

print(get_int_vlan_map('config_sw2.txt'))