# servomotoros teszt sajnos nem müködtek.
from ev3dev.auto import OUTPUT_A, MediumMotor
import time
#import ev3dev.ev3 as ev3
m = MediumMotor(OUTPUT_A)
ciklus = 0
elore = 100

m.stop_action = "hold"
m.position_sp = 90
m.run_to_abs_pos()
