import netmiko


class CiscoSSH:
    def __init__(self, **device_params):
        self.ssh = netmiko.ConnectHandler(**device_params)
        self.ssh.enable()

    def send_show_command(self, command):
        return self.ssh.send_command(command)

    @staticmethod
    def parse_show(command, command_output,
                   index_file='index', templates='templates'):
        attributes = {'Command': command,
                      'Vendor': 'cisco_ios'}
        cli_table = clitable.CliTable(index_file, templates)
        cli_table.ParseCmd(command_output, attributes)
        return [dict(zip(cli_table.header, row)) for row in cli_table]

