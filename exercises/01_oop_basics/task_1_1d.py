# -*- coding: utf-8 -*-

'''
Задание 1.1d

Изменить класс Topology из задания 1.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще нет в топологии
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение "Cоединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Cоединение с одним из портов существует


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

    def add_link(self, port1, port2):
        if port1 in self.topology:
            if self.topology[port1] == port2:
                print('Такое соединение существует')
            else:
                print('Cоединение с одним из портов существует')
        else:
            self.topology[port1] = port2

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
t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
pprint(t.topology)
t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
