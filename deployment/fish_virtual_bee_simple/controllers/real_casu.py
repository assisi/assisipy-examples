#! /usr/bin/env python
# -*- coding: utf-8 -*-

from assisipy import sim, casu

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from time import sleep

from assisipy import bee, casu

if __name__ == '__main__':
    
    cook_ref = 35
    cool_ref = 28

    c = casu.Casu(sys.argv[1],log=True)

    while(1):
        temp = c.get_temp(casu.TEMP_WAX)
        if temp > 32:
            print('Sending cooking order!')
            c.send_message('virtual','cook')
        elif temp < 29:
            print('Sending cooling order!')
            c.send_message('virtual','cool')

        msg = c.read_message()
        if msg:
            if 'virtual' in msg.keys():
                data = msg['virtual']
                if data == 'cook':
                    c.set_diagnostic_led_rgb(r=1)
                    print('Cooking to {0}C'.format(cook_ref))
                    c.set_temp(cook_ref)
                elif data == 'cool':
                    c.set_diagnostic_led_rgb(b=1)
                    print('Cooling to {0}C'.format(cool_ref))
                    c1.set_temp(cool_ref)

        sleep(1)
