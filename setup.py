# setup.py - set up all the hardware components (potentiometer, buttons, LCD, sensors) and initialize the necessary variables.
from machine import Pin, I2C
import i2c_lcd
import time

# Pin initialization
potentiometer = machine.ADC(machine.Pin(26))  # Pin for potentiometer
button1 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)  # Button1 for decreasing temp_min
button2 = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)  # Button2 for increasing temp_max
switch = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)  # Switch for enabling/disabling loop

# Sensor initialization (e.g., DHT22 for humidity and temperature)
sensor = machine.DHT(machine.Pin(14), machine.DHT22)  # Replace with actual pin

# LCD initialization (you should have an LCD library)
lcd.init()

# Initial variable setup
temp_min = 20
temp_max = 30
humid_max = 70
humid_thresh = humid_max * 0.75

# Interval mapping function
def interval_mapping(value, in_min, in_max, out_min, out_max):
    """Maps a value from one range to another."""
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
