import netmiko


class CiscoSSH:
    def __init__(self, **device_params):
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()

    def send_show_command(self, command):
        return self.ssh.send_command(command)

    @classmethod
    def default_params(cls, ip):
        params = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': 'cisco',
            'password': 'cisco',
            'secret': 'cisco'}
        return cls(**params)

