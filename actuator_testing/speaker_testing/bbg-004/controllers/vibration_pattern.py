#!/usr/bin/env python
# A program for testing the vibration actuator

import time
import argparse

from assisipy import casu


if __name__ == '__main__':


    parser = argparse.ArgumentParser(description="Test casu vibration patterns.")
    parser.add_argument('rtc_file', help='Name of the Casu rtc file.')
    args = parser.parse_args()

    T_experiment = 1800 # Total experiment duration (1/2h)

    mycasu = casu.Casu(args.rtc_file)

    vibe_periods = [1000,100]
    vibe_freqs = [440,1]
    vibe_amps = [50,0]
    
    print('{0} setting vibration pattern {1},{2},{3}'.format(mycasu.name(),
                                                             vibe_periods,
                                                             vibe_freqs,
                                                             vibe_amps))
    time_start = time.time()
    mycasu.set_vibration_pattern(vibe_periods,vibe_freqs,vibe_amps)
    time.sleep(T_experiment)
    mycasu.speaker_standby()
    print(mycasu.name() + ' done!')

    
