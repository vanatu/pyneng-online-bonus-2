import netmiko


class CiscoSSH:
    def __init__(self, **device_params):
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()
        self.__cfg = None

    def send_show_command(self, command):
        return self.ssh.send_command(command)

    @property
    def cfg(self):
        if not self.__cfg:
            self.__cfg = self.send_show_command('sh run')
        return self.__cfg


## property setter

class CiscoSSH:
    def __init__(self, **device_params):
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()
        self.__mgmt_ip = None

    @property
    def mgmt_ip(self):
        if not self.__mgmt_ip:
            loopback0 = self.ssh.send_command('sh run interface lo0')
            self.__mgmt_ip = re.search('ip address (\S+) ', loopback0).group(1)
        return self.__mgmt_ip

    @mgmt_ip.setter
    def mgmt_ip(self, new_ip):
        if self.mgmt_ip != new_ip:
            self.ssh.send_config_set(['interface lo0',
                                      'ip address {} 255.255.255.255'.format(new_ip)])
            self.__mgmt_ip = new_ip


