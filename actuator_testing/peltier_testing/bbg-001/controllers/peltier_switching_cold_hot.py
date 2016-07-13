#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

from assisipy import casu

if __name__ == '__main__':

    c = casu.Casu(sys.argv[1])

    time_begin = time.time()
    time_now = time.time()

    while(time_now - time_begin < 1800):

        c.set_temp(28)
        c.set_diagnostic_led_rgb(b=1)
        time.sleep(300)

        c.set_temp(35)
        c.set_diagnostic_led_rgb(r=1)
        time.sleep(300)
        
        time_now = time.time()
