
from ev3dev.auto import *
import time
m = Motor(OUTPUT_A)
ir = InfraredSensor()
#m.reset()  a position resetje is egyben. Az aktuális lesz a position = 0 
szog = 90
# jelenlegi position kiiratása 
print m.position 
while True :
	# absolute pozicióhoz megy. duty_cycle_sp a motor sebessége 
        m.run_to_abs_pos( position_sp=szog,stop_command = 'brake',duty_cycle_sp=25)
	
	# amint eléri a kivánt 90 fokot a szoget negálja és így az ellenkező irányba fog elindulni
        if m.position < szog+10 and m.position >szog-10:
                print "OK!"
                szog = (szog * (-1))
		#infrasensor mérései és visszajelzései
        if ir.value() > 60:
                if m.position > 60:
                        print "Jobbra szabad."
                elif m.position < 60 and m.position > -60:
                        print "Elore."
                elif m.position < -60:
                        print "Balra szabad."








