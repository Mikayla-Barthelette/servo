# Created by: Mikayla Barthelette
# Created on: Oct. 2020
# 
# This program allows us to make a servo turn 180 degrees


#load microbit module for python
from microbit import *

def set_servo_pulse(pin, ms_on):
    pin.write_analog(1023 * ms_on / 20)
    
def init_servo_pin(pin):
    pin.set_analog_period(20)
    set_servo_pulse(pin, 1.5)
    
def main():
    init_servo_pin(pin8)
    set_servo_pulse(pin8, 1.0)
    sleep(1000)
    set_servo_pulse(pin8, 2.0)
    
#display heart to confirm connectivity
display.show(Image.HEART)

#rotate servo 180 degrees 6 times
count = 0
while (count < 7):     
    count = count + 1
    main()
    sleep(1000)
    

