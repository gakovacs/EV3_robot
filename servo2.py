# servo motoros teszt ( második) sajnos ez sem müködött
from ev3dev.auto import OUTPUT_A, ServoMotor

m = ServoMotor(OUTPUT_A)
m.position_sp = 100
m.run()

