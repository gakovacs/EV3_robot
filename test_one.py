from ev3dev.auto import OUTPUT_A, Motor
import time
#motor előre megy 1 másodpercig teljes sebességel ( csak az egyik motor ) 
m = Motor(OUTPUT_A)
m.run_forever(duty_cycle_sp = 100)
time.sleep(1)
m.stop()
