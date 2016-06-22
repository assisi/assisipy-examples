#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import randrange
from math import pi, copysign
from time import sleep

from assisipy import sim, bee

if __name__ == '__main__':

    t_limit = 30

    # Limits of bee motion
    xmin_left = -10
    xmax_left = -3
    xmin_right = 3
    xmax_right = 10
    
    # Start on the left side
    xmin = xmin_left
    xmax = xmax_left
    ymin = -10
    ymax = 10

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
        
        if t > t_limit:
            print("It's gettin hot in here!")
            # Switch sides
            if (xmin + xmax) < 0:
                # left -> right
                xmin = xmin_right
                xmax = xmax_right
            else:
                # right -> left
                xmin = xmin_left
                xmax = xmax_left
        sleep(1)
