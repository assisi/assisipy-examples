#!/usr/bin/env python
# A program for testing the vibration actuator

import time
import argparse

from assisipy import casu


if __name__ == '__main__':


    parser = argparse.ArgumentParser(description="Test casu heat actuator.")
    parser.add_argument('rtc_file', help='Name of the Casu rtc file.')
    args = parser.parse_args()

    T_experiment = 1800 # Total experiment duration (1h)

    mycasu = casu.Casu(args.rtc_file)
    
    time_start = time.time()
    time_cycle_start_temp = time_start
    time_now = time.time()
    t_on = 1.0  # vibration on
    t_off = 0.1 # vibration off
    state = 0
    vibe_counter = 0
    while time_now - time_start < T_experiment:
        t_loop_start = time.time();
        if state == 0:
            state = 1
            vibe_amp = 50
            vibe_freq = 440
            t_delay = t_on
        else:
            state = 0
            vibe_amp = 0
            vibe_freq = 440
            t_delay = t_off

        mycasu.set_speaker_vibration(freq=vibe_freq,intens=vibe_amp)
        time_now = time.time()
        time.sleep(t_delay - (time.time() - t_loop_start))
    mycasu.set_speaker_vibration(freq=0,intens=0)
    
