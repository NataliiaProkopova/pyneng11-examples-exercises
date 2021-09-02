# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv
filename_from = argv[1]
filename_where = argv[2]

with open(filename_from, 'r') as f, open (filename_where, 'w') as dest:
    for line in f:
        valid = True
        if line.startswith('!'):
            valid = False
        for word in ignore:
            if line.count(word):
                valid = False
        if valid:
            dest.write(line)
            #print(line.rstrip())