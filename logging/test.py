
from assisipy import casu
from time import sleep

casu1 = casu.Casu('casu-004.rtc')
ir  = [0 for i in range(7)]
temp = [0 for i in range(5)]

casu1.set_vibration_freq(300)
casu1.set_temp(30)

while True:
    for i in range(7):
        ir[i] = casu1.get_ir_raw_value(i)
    for i in range(5):
        temp[i] = casu1.get_temp(casu.TEMP_F + i)
    print(ir)
    print(temp)
    sleep(1)

