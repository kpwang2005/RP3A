### TonalBuzzer not support PiGPIO 
#from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import TonalBuzzer
from time import sleep

#tones = ["C4", "E4", "G4"]
tones = ["G4", "C4", "A4", "F4", "E4", "C4", "D4"]

tbz = TonalBuzzer(12)

for tone in tones:
    tbz.play(tone)
    sleep(1)
    tbz.stop()
    sleep(0.1)
    


