from gpiozero import DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory()

sensor = DistanceSensor(echo=18, trigger=17, pin_factory=factory)
while True:
    print('Distance: ', sensor.distance * 100)
    sleep(1)
