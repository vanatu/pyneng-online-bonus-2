# -*- coding: utf-8 -*-

'''
Задание 1.1c

Изменить класс Topology из задания 1.1b.

Добавить метод delete_node, который удаляет все соединения с указаным устройством.

Если такого устройства нет, выводится сообщение "Такого устройства нет".

Создание топологии
In [1]: t = Topology(topology_example)

In [2]: t.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Удаление устройства:
In [3]: t.delete_node('SW1')

In [4]: t.topology
Out[4]:
{('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

Если такого устройства нет, выводится сообщение:
In [5]: t.delete_node('SW1')
Такого устройства нет

'''
from pprint import pprint

class Topology:
    def __init__(self, topology_dict):
        self.topology = {}
        for k,v in topology_dict.items():
            if k not in self.topology.values():
                self.topology[k] = v

    def delete_link(self, port1, port2):
        if port1 in self.topology:
            del self.topology[port1]
        elif port2 in self.topology:
            del self.topology[port2]
        else:
            print('Такого соединения нет')

    def delete_node(self, node):
        topology = self.topology.copy()
        self.topology = dict(filter(lambda x: node not in [i for j in x for i in j], self.topology.items()))
        if topology == self.topology:
            print('Такого устройства нет')

topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}

t = Topology(topology_example)
pprint(t.topology)
t.delete_node('SW1')
pprint(t.topology)
t.delete_node('SW1')
