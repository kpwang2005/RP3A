from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import PWMLED
from time import sleep

factory = PiGPIOFactory()

led = PWMLED(12, pin_factory=factory)
"""
while True:
    for duty in range(0,100,1):
        led.value = duty/100.0
        sleep(0.05)
    for duty in range(100,0,-1):
        led.value = duty/100.0
        sleep(0.05)
"""
led.pulse(2,2,n=5,background=False)
