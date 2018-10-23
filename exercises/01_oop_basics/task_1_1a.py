# -*- coding: utf-8 -*-
from pprint import pprint
'''
Задание 1.1a

Изменить класс Topology из задания 1.1.

Если в задании 1.1 удаление дублей выполнялось в методе __init__,
надо перенести функциональность удаления дублей в метод _normalize.

Метод __init__ должен выглядеть таким образом:
'''

class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def _normalize(self, topology_dict):
        result = {}
        for k,v in topology_dict.items():
            if k not in result.values():
                result[k] = v
        return result

topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}

top = Topology(topology_example)
pprint(top.topology)
