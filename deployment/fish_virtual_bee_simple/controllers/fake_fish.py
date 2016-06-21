#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import randrange
from math import pi, copysign
from time import sleep

from assisipy import sim, bee

if __name__ == '__main__':

    # Inital limits of bee motion
    xmin = 0
    xmax = 15
    ymin = -15
    ymax = 15

    sim_ctrl = sim.Control(pub_addr='tcp://control-workstation:5556',
                           sub_addr='tcp://control-workstation:5555')

    b1 = bee.Bee(name='bee-001',
                  pub_addr='tcp://control-workstation:5556',
                  sub_addr='tcp://control-workstation:5555')

    while(1):
        x = randrange(xmin,xmax)
        y = randrange(ymin,ymax)
        yaw = randrange(-3,3)
        sim_ctrl.teleport('bee-001',(x,y,yaw))

        t = b1.get_temp(bee.TEMP_SENSOR_FRONT)
        
        if t > 30:
            print("It's gettin hot in here!")
            # Switch sides
            xmin = xmin - copysign(15,xmin+xmax)
            xmax = xmax - copysign(15,xmin,xmax)

        sleep(1)
