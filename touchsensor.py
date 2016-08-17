from ev3dev.auto import OUTPUT_A, OUTPUT_B,Motor
import ev3dev.ev3 as ev3
import time
# a az egyik motor b a másik ts pedig a touchsensor
ts = ev3.TouchSensor()
a = Motor(OUTPUT_A)
b = Motor(OUTPUT_B)
# előre megy majd ütközik, megáll és hátramegy.

while True :
    a.run_forever(duty_cycle_sp = 100)
    b.run_forever(duty_cycle_sp = 100)

    if ts.value():
        a.stop()
        b.stop()
        time.sleep(1)
        a.run_timed(time_sp=1000, duty_cycle_sp=-75)
        b.run_timed(time_sp=1000, duty_cycle_sp=-75)
        time.sleep(2)
        a.run_timed(time_sp=1500, duty_cycle_sp=75)


   
