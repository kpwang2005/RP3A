from gpiozero import DistanceSensor
from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()

sensor = DistanceSensor(echo=18, trigger=17, pin_factory=factory)

led = PWMLED(13, pin_factory=factory)

while True:
    print('Distance: ', sensor.distance * 100)
    if sensor.distance < 0.3:
        led.blink(0.2, 0.2)
    else:
        led.off()
    sleep(2)
