from ev3dev.auto import OUTPUT_A, OUTPUT_B, Motor
import time
# robot forgásának tesztelése
m = Motor(OUTPUT_A)
k = Motor(OUTPUT_B)
m.run_forever(duty_cycle_sp = 100)
k.run_forever(duty_cycle_sp = -100)
time.sleep(2)
m.stop()
k.stop()
