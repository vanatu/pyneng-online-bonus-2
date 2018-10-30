# -*- coding: utf-8 -*-

'''
Задание 1.2a

Изменить класс CiscoSSH из задания 1.2:

* добавить метод send_show_command, который повторяет функциональность метода send_command netmiko


Пример создания экземпляра класса:
In [2]: r1 = CiscoSSH('cisco', 'cisco', 'cisco', '192.168.100.1')

Использование метода send_show_command:
In [3]: r1.send_show_command('sh ip int br')
Out[3]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '



'''
import netmiko

class HuaweiSSH:
    def __init__(self, ip, username, password):
        device_dict = {'device_type':'huawei',
        'username': username,
        'password': password,
        'ip': ip}

        self.ssh = netmiko.ConnectHandler(**device_dict)

    def send_show_command(self, command):
        return self.ssh.send_command(command)

r1 = HuaweiSSH('192.168.0.110', 'lab', 'Lab123')

print(r1.send_show_command('display ip int br'))
