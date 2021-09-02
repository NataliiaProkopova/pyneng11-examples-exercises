# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

output = []
with open('CAM_table.txt') as f:
    for line in f:
        if (line !='\n'):
            params = line.split()
            if params[0].isdigit():
                params[0] = int(params[0])
                output.append(params)
output = sorted(output)

vlan = input('Введите номер VLAN: ')

for line in output:
    if int(vlan) == line[0]:
        print('{:<10}{:<20}{:<10}'.format(line[0],line[1],line[3]))