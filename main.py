# main.py

import time
from setup import *  # Import everything from setup.py

while True:
    # Read potentiometer and map it to a 0-100 range
    value = interval_mapping(potentiometer.read_u16(), 0, 65535, 0, 100)
    humid_max = int(value)
    humid_thresh = int(humid_max * 0.75)
