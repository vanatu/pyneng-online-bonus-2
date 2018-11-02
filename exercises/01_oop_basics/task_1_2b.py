# -*- coding: utf-8 -*-

'''
Задание 1.2b

Изменить класс CiscoSSH из задания 1.2a.

Добавить метод send_and_parse_show, который:
    1. отправляет команду show на оборудование
    2. получает результат
    3. парсит его с помощью TextFSM
    4. возвращает результат в виде списка словарей

Для отправки команды и получения ее результата должен использоваться метод send_show_command.

Шаблон TextFSM должен выбираться динамически, на основании команды.


Пример создания экземпляра класса:
In [2]: r1 = CiscoSSH('cisco', 'cisco', 'cisco', '192.168.100.1')

Использование метода send_and_parse_show:
In [3]: r1.send_and_parse_show('sh ip int br')
Out[3]:
[{'ADDR': '192.168.100.1',
  'INT': 'Ethernet0/0',
  'PROTO': 'up',
  'STATUS': 'up'},
 {'ADDR': '192.168.200.1',
  'INT': 'Ethernet0/1',
  'PROTO': 'up',
  'STATUS': 'up'},
 {'ADDR': '190.16.200.1', 'INT': 'Ethernet0/2', 'PROTO': 'up', 'STATUS': 'up'},
 {'ADDR': '192.168.230.1',
  'INT': 'Ethernet0/3',
  'PROTO': 'up',
  'STATUS': 'up'}]

Использование метода send_and_parse_show с явным указанием всех параметров:
In [4]: r1.send_and_parse_show('sh ip int br', index_file='index', templates_dir='templates')
Out[4]:
[{'ADDR': '192.168.100.1',
  'INT': 'Ethernet0/0',
  'PROTO': 'up',
  'STATUS': 'up'},
 {'ADDR': '192.168.200.1',
  'INT': 'Ethernet0/1',
  'PROTO': 'up',
  'STATUS': 'up'},
 {'ADDR': '190.16.200.1', 'INT': 'Ethernet0/2', 'PROTO': 'up', 'STATUS': 'up'},
 {'ADDR': '192.168.230.1',
  'INT': 'Ethernet0/3',
  'PROTO': 'up',
  'STATUS': 'up'}]

'''
import netmiko, clitable
from pprint import pprint

class HuaweiSSH:
    def __init__(self, ip, username, password):
        device_dict = {'device_type':'huawei',
        'username': username,
        'password': password,
        'ip': ip}

        self.ssh = netmiko.ConnectHandler(**device_dict)

    def send_show_command(self, command):
        return self.ssh.send_command(command)

    def send_and_parse_show(self, command, index_file='index', templates_dir='templates'):
        output = self.send_show_command(command)
        cli_table = clitable.CliTable(index_file, templates_dir)
        attributes = {'Vendor':'huawei'}
        cli_table.ParseCmd(output, attributes)
        keys = list(cli_table.header)
        rows = [row for row in cli_table]
        return [{k:v for k, v in zip(keys,row)} for row in rows]

r1 = HuaweiSSH('192.168.0.110', 'lab', 'Lab123')

pprint(r1.send_and_parse_show('display ip int br', index_file='index', templates_dir='templates'))
