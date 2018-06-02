import sqlite3
from collections import namedtuple


key = 'vlan'
value = 10
db_filename = 'dhcp_snooping.db'

keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
DhcpSnoopRecord = namedtuple('DhcpSnoopRecord', keys)

conn = sqlite3.connect(db_filename)
query = 'select {} from dhcp where {} = ?'.format(','.join(keys), key)

print('-' * 40)
result = conn.execute(query, (value,))
named_t = map(DhcpSnoopRecord._make, result)
#named_t = [DhcpSnoopRecord._make(i) for i in result]
#DhcpSnoopRecord._make(('A', '10.1.1.1, '10'))

for row in named_t:
    print(row)
    print(row.mac, row.ip, row.interface, sep='\n')
    print('-' * 40)


result = conn.execute(query, (value,))

for row in result:
    record = DhcpSnoopRecord(*row)
    print(record.mac, record.ip, record.interface, sep='\n')
    print('-' * 40)
