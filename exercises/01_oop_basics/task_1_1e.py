# -*- coding: utf-8 -*-

'''
Задание 1.1e

Изменить класс Topology из задания 1.1x.

Добавить метод, который позволит выполнять сложение двух объектов (экземпляров) Topology.
В результате сложения должен возвращаться новый экземпляр класса Topology.

In [1]: t1 = Topology(topology_example)

In [2]: t1.topology
Out[2]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [3]: topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                             ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

In [4]: t2 = Topology(topology_example2)

In [5]: t2.topology
Out[5]: {('R1', 'Eth0/4'): ('R7', 'Eth0/0'), ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

In [6]: t3 = t1+t2

In [7]: t3.topology
Out[7]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R1', 'Eth0/6'): ('R9', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}


'''
from pprint import pprint

class Topology:
    def __init__(self, topology_dict):
        self.topology = {}
        for k,v in topology_dict.items():
            if k not in self.topology.values():
                self.topology[k] = v

    def __add__(self, other):
        return Topology({**self.topology, **other.topology})

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

topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                     ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}

t1 = Topology(topology_example)
pprint(t1.topology)
t2 = Topology(topology_example2)
pprint(t2.topology)
t3 = t1+t2
pprint(t3.topology)
