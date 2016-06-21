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
        temp = b1.get_temp(casu.TEMP_WAX)
        if temp > 32:
            c.set_diagnostic_led_rgb(r=1)
            c.send_message('virtual','cook')
        elif temp < 29:
            c.set_diagnostic_led_rgb(b=1)
            c.send_message('virtual','cool')

        msg = c.get_message()
        if msg:
            if 'virtual' in msg.keys():
                data = msg['virtual']
                if data == 'cook':
                    print('Cooking to {0}C'.format(cook_ref))
                    c.set_temp(cook_ref)
                elif data == 'cool':
                    print('Cooling to {0}C'.format(cool_ref))
                    c1.set_temo(cool_ref)

        sleep(1)
