# -*- coding: utf-8 -*-

'''
Задание 1.2c

Изменить класс CiscoSSH из задания 1.2b:
* добавить метод send_cfg_commands, который повторяет функциональность метода send_config_set netmiko

Пример создания экземпляра класса:
In [2]: r1 = CiscoSSH('cisco', 'cisco', 'cisco', '192.168.100.1')

Использование метода send_cfg_commands:
In [3]: r1.send_cfg_commands('logging 10.1.1.1')
Out[3]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#logging 10.1.1.1\nR1(config)#end\nR1#'

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

    def send_cfg_commands(self, command):
        return self.ssh.send_config_set(command)

    def send_and_parse_show(self, command, index_file='index', templates_dir='templates'):
        output = self.send_show_command(command)
        cli_table = clitable.CliTable(index_file, templates_dir)
        attributes = {'Vendor':'huawei', 'Command':command}
        cli_table.ParseCmd(output, attributes)
        keys = list(cli_table.header)
        rows = [row for row in cli_table]
        return [{k:v for k, v in zip(keys,row)} for row in rows]

r1 = HuaweiSSH('192.168.0.110', 'lab', 'Lab123')

pprint(r1.send_cfg_commands('header shell information "Hello"'))
