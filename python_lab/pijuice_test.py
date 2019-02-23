from pijuice import PiJuice

pijuice = PiJuice(1, 0x14)

print(pijuice.status.SetLedState('D2', [0, 0, 0]))
print(pijuice.status.SetLedBlink('D2', 10,[100, 0, 0], 500, [0, 100, 0], 500))
# count=255 -> indefinite
