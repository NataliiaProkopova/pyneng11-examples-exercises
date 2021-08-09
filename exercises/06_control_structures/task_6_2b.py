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




while True:
    ip_addr = input('Введите IP-адрес в формате 10.1.1.1: ')
    octets = ip_addr.split('.')
    valid_ip = True
    if (len(octets)!=4):
        valid_ip=False
    for oct in octets:
        if not (oct.isdigit() and (int(oct) in range(256))):
            valid_ip=False
            break
    if valid_ip:
        break
    else:
        print('Неправильный IP-адрес')

oct1 = int(octets[0])
if  oct1>0 and oct1<=223:
    print('unicast')
elif oct1>223 and oct1<=239:
    print('multicast')
elif ip_addr == '255.255.255.255':
    print('local broadcast')
elif ip_addr == '0.0.0.0':
    print('unassigned')
else:
    print('unused')