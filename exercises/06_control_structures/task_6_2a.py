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

ip_addr = input('Введите IP-адрес в формате 10.1.1.1: ')
octets = ip_addr.split('.')
valid_ip = True
if (len(octets)!=4):
    valid_ip=False
for oct in octets:
    if not (oct.isdigit() and (int(oct) in range(256))):
        valid_ip=False
        break
if not valid_ip:
   print('Неправильный IP-адрес')
else:
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