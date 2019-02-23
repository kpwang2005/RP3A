from gpiozero import DistanceSensor
from gpiozero import PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
from pijuice import PiJuice

factory = PiGPIOFactory()

sensor = DistanceSensor(echo=18, trigger=17, pin_factory=factory)

#led = PWMLED(13, pin_factory=factory)
pijuice = PiJuice(1, 0x14)

while True:
    print('Distance: ', sensor.distance * 100)
    if sensor.distance < 0.3:
        #led.blink(0.2, 0.2)
        pijuice.status.SetLedBlink('D2', 2,[100, 0, 0], 500, [0, 100, 0], 500)
    else:
        #led.off()
        pijuice.status.SetLedState('D2', [0, 0, 0])
    sleep(2)
