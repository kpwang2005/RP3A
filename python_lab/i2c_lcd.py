from RPLCD.i2c import CharLCD
from time import sleep

lcd = CharLCD('PCF8574', address=0x27, port=1)

lcd.clear()
lcd.cursor_pos = (0, 0)
lcd.write_string("hihi")
lcd.cursor_pos = (1, 6)
lcd.write_string("codecs")

#lcd.backlight_enabled = True
sleep(2)
lcd.backlight_enabled = False

