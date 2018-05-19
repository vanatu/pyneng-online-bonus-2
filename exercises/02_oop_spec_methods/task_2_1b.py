# -*- coding: utf-8 -*-

'''
Задание 2.1b

Добавить к классу CiscoTelnet из задания 2.1 или 2.1a поддержку работы в менеджере контекста.
При выходе из блока менеджера контекста должно закрываться соединение.
Все исключения, которые возникли в менеджере контекста, должны генерироваться после выхода из блока with.


In [1]: from task_2_1b import CiscoTelnet

In [2]: with CiscoTelnet('192.168.100.1', 'cisco', 'cisco', 'cisco') as r1:
   ...:     print(r1.send_show_command('sh clock'))
   ...:
sh clock
*13:15:44.286 UTC Sat May 19 2018
R1#

In [3]: with CiscoTelnet('192.168.100.1', 'cisco', 'cisco', 'cisco') as r1:
   ...:     print(r1.send_show_command('sh clock'))
   ...:     raise ValueError('Возникла ошибка')
   ...:
sh clock
*13:15:36.062 UTC Sat May 19 2018
R1#
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-2-f93c2f0d4e85> in <module>()
      1 with CiscoTelnet('192.168.100.1', 'cisco', 'cisco', 'cisco') as r1:
      2     print(r1.send_show_command('sh clock'))
----> 3     raise ValueError('Возникла ошибка')

ValueError: Возникла ошибка


'''

