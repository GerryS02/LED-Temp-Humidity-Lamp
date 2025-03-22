# LED-Temp-Humidity-Lamp (Temperature and Humidity Indicator)

## Overview
This project is an LED color-changing lamp that responds to changes in temperature and humidity using a Raspberry Pi and a DHT11 sensor. The lamp serves as a visual indicator to ensure an environment stays within the desired temperature and humidity range.

## Features
- **Primary Function**: Temperature and humidity indication.
- **DHT11 Sensor**: Detects temperature and humidity.
- **LCD Display**: Shows temperature and humidity readings.
- **RGB LED Light**: Indicates whether the values are within the acceptable range.
- **Two Modes of Operation**:
  - **Edit Mode**: Allows the user to set humidity limits and temperature range.
  - **Sense Mode**: Displays real-time temperature and humidity, and adjusts the LED color accordingly.

## Components
- Raspberry Pi.
- DHT11 Sensor.
- RGB LED.
- LCD Display.
- Potentiometer.
- Slide Switch.
- Two Buttons.

## Functionality
### Edit Mode
- The potentiometer sets the humidity limit.
- Two buttons allow changing the temperature range.
- The LCD displays the set limits.

### Sense Mode
- The LCD displays the current temperature and humidity.
- The LED color changes based on the sensor readings:
  - Green when within range.
  - Fades from green to red as humidity exceeds 75% of the limit.
  - Turns red immediately when the temperature is outside the default range (10°C - 30°C).

## Use Cases
- Ensuring optimal conditions for plant growth.
- Monitoring storage environments for sensitive materials.
- Maintaining comfortable indoor conditions.

## Installation
1. Connect the DHT11 sensor, LCD, RGB LED, potentiometer, slide switch, and buttons to the Raspberry Pi.
2. Load the project code onto the Raspberry Pi.
3. Power on the system and use the slide switch to toggle between Edit and Sense modes.

<hr>
https://github.com/GerryS02/LED-Temp-Humidity-Lamp/blob/b49318c9d47bb5e9acb44f376642818c024a3a40/Screenshot%202025-03-17%20122851.png
