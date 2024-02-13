import RPi.GPIO as GPIO
from pad4pi import rpi_gpio
import time
import smbus2  # For I2C communication with PCF8574T

# ... (Keypad, Display, other global variables settings)

# -------- LCD (Hypothetical, adjust per your library!) ----------
def lcd_init():
    # ... commands specific to your I2C library ....

def lcd_clear():
    i2c_bus.write_byte_data(LCD_I2C_ADDRESS, 0x00, 0x01)  # Now indented under the function

def lcd_string(message, line):
    lcd_clear()
    message = message.ljust(LCD_CHARS," ")
    for i in range(LCD_CHARS):
        i2c_bus.write_byte_data(LCD_I2C_ADDRESS, 0x40, ord(message[i]))

# ----- Keypad Handling --------
def print_key(key):
    #  ... (Your existing key handling logic) ...

# ------------------- Main Initialization --------------
lcd_init()  # Call the LCD initialization

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD)  # Create the keypad

# Set keypad row and column pins - Based on dir(keypad) output
keypad._row_pins = ROW_PINS
keypad._col_pins = COL_PINS

keypad.registerKeyPressHandler(print_key)

print("Select a Plant with Key 1, 2, or 3, then Set Moisture level. Ctrl+C to exit")

while True:
    time.sleep(1)

