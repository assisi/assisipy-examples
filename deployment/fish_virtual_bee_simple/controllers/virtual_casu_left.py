#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from time import sleep

from assisipy import bee, casu

if __name__ == '__main__':

    b1 = bee.Bee(name='bee-001',
                 pub_addr='tcp://control-workstation:5556',
                 sub_addr='tcp://control-workstation:5555')
    
    c1 = casu.Casu(sys.argv[1],log=True)

    while(1):
        (x,y,yaw) = b1.get_true_pose()
        if x < 0:
            c1.set_diagnostic_led_rgb(r=1)
            c1.send_message('real','cook')
            print('{0} sending a cooking order.'.format(c1.name())
        else:
            c1.set_diagnostic_led_rgb(b=1)
            c1.send_message('real','cool')
            print('{0} sending a cooling order.'.format(c1.name())

        msg = c1.get_message()
        if msg:
            if 'real' in msg.keys():
                data = msg['real']
                if data == 'cook':
                    c1.set_temp(35)
                  print('{0} got a cooking order.'.format(c1.name())
                elif data == 'cool':
                    c1.set_temo(28)
                    print('{0} got a cooling order.'.format(c1.name())

        sleep(1)
