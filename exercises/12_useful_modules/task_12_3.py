# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""

from task_12_1 import ping_ip_addresses
from tabulate import tabulate

def print_ip_table (reach_list, unreach_list):
    ip_dict={}
    ip_dict['Reachable'] = reach_list
    ip_dict['Unreachable'] = unreach_list
    print(tabulate(ip_dict, headers='keys'))

if __name__ == '__main__':
    list = ['8.8.8.8', '1.1.1.a','8.8.4.4','192.168.1.1']
    reach, unreach = ping_ip_addresses(list)
    print_ip_table (reach, unreach)