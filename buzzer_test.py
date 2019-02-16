from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Buzzer
from gpiozero import PWMLED
from time import sleep

# for Buzzer
"""
bz = Buzzer(12)
bz.beep(n=3, background=False)
"""

# pseudo tonal buzzer
tones = [392, 262, 440, 349, 330, 262, 294]

factory = PiGPIOFactory()
led = PWMLED(12,pin_factory=factory)

for tone in tones:
    led.frequency = tone
    led.value = 0.1
    sleep(1)

led.off()
