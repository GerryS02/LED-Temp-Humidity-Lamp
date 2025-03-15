# main.py - contain the main loop logic that controls the behavior of the program

import time
from setup import *  # Import everything from setup.py

while True:
    # Read potentiometer and map it to a 0-100 range
    value = interval_mapping(potentiometer.read_u16(), 0, 65535, 0, 100)
    humid_max = int(value)
    humid_thresh = int(humid_max * 0.75)

    # If button1 is pressed, decrease temp_min and update display
    if button1.value() == 1:
        timeframe = time.ticks_add(time.ticks_ms(), 500)
        while time.ticks_diff(timeframe, time.ticks_ms()) > 0 and button1.value() == 0:
            time.sleep_ms(500)
        while button1.value() == 1:
            temp_min -= 1
            lcd.message("Humidity Max:{}\nTemp: {}C-{}".format(humid_max, temp_min, temp_max))
            time.sleep_ms(200)
            lcd.clear()
            time.sleep_ms(25)
        break

    # If button1 is pressed again, increase temp_min
    elif button1.value() == 1:
        temp_min += 1
        lcd.message("Humidity Max:{}\nTemp: {}C-{}".format(humid_max, temp_min, temp_max))
        time.sleep_ms(200)
        lcd.clear()
        time.sleep_ms(25)

    # If button2 is pressed, increase temp_max and update display
    elif button2.value() == 1:
        while True:
            timeframe = time.ticks_add(time.ticks_ms(), 500)
            while time.ticks_diff(timeframe, time.ticks_ms()) > 0 and button2.value() == 0:
                time.sleep_ms(500)
            if button2.value() == 1:
                temp_max += 1
                lcd.message("Humidity Max:{}\nTemp: {}C-{}".format(humid_max, temp_min, temp_max))
                time.sleep_ms(200)
                lcd.clear()
                time.sleep_ms(25)
            break

    # If button2 is pressed again, just update the display
    elif button2.value() == 1:
        lcd.message("Humidity Max:{}\nTemp: {}C-{}".format(humid_max, temp_min, temp_max))
        time.sleep_ms(200)
        lcd.clear()
        time.sleep_ms(25)

    # If switch is off, sleep for 1 second
    if switch.value() == 0:
        time.sleep(1)

# Main loop when switch is on
while switch.value() == 0:
    # Measure sensor values
    sensor.measure()
    worse = int(interval_mapping(sensor.humidity(), humid_thresh, humid_max, 0, 255))
    bad = int(interval_mapping(sensor.humidity(), humid_thresh, humid_max, 255, 0))

    # If humidity or temperature is out of range, set red color (warning)
    if (sensor.humidity() >= humid_max) or (sensor.temperature() >= temp_max or sensor.temperature() <= temp_min):
        color_set(255, 0, 0)

    # If humidity is too low, set a warning color (yellow/orange)
    elif (sensor.humidity() <= humid_thresh):
        color_set(worse, bad, 0)

    # Otherwise, set green color (safe)
    else:
        color_set(0, 255, 0)

    # Display temperature and humidity
    lcd.message("Temp: {}C\nHumidity: {}%".format(sensor.temperature(), sensor.humidity()))
    time.sleep(1)
    lcd.clear()



