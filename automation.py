import RPi.GPIO as pins
import time

pins.setmode(pins.BCM)

# Set pins
# I may be able to automate this, too, by getting the data first, then assigning the pin to a sensor-type based on the date that's being received.
temperatureSensorPin = 0
humiditySensorPin = 0
airQualitySensorPin = 0
heaterRelayPin = 0
heaterRelayStatus = pins.LOW
humidifierRelayPin = 12
humidifierRelayStatus = pins.LOW
humidifierRelayStatusText = "pins.LOW"

# Set important limits
minTemp = 76     # in Fahrenheit
maxTemp = 79     # in Fahrenheit
minHumidity = 90     # in percentage
maxHumidity = 95     # in percentage

# How often do you want to record data to the backend (in seconds)?
dataRecordingInterval = 600 #every 5 minutes, though, currently this does not necessarily correspond to 5 minutes.

# Relay
pins.setup(heaterRelayPin, pins.OUT)
pins.output(heaterRelayPin, heaterRelayStatus)

try:
  printTimer = 0
  while True:
        
    # Get data
    # temperatureReading = temperatureSensorPin.whatever
    # humidityReading = humiditySensorPin.whatever
    # airQualityReading = airQualitySensorPin.whatever
    
    # Handle the heater relay.
    # if (temperatureReading < minTemp):
    #   # Turn on the heater by activating the relay
    #   heaterRelayStatus = pins.HIGH
    #   pins.output(heaterRelayPin, heaterRelayStatus)
    # elif (temperatureReading >= maxTemp - 1):
    #   # Turn on the heater by activating the relay
    #   heaterRelayStatus = pins.LOW
    #   pins.output(heaterRelayPin, heaterRelayStatus)
    
    # # Handle the humidifier relay.
    # if (humidityReading < minHumidity):
    #   # Turn on the heater by activating the relay
    #   heaterRelayStatus = pins.HIGH
    #   pins.output(heaterRelayPin, heaterRelayStatus)
    # elif (humidityReading >= maxHumidity - 1):
    #   # Turn on the heater by activating the relay
    #   heaterRelayStatus = pins.LOW
    #   pins.output(heaterRelayPin, heaterRelayStatus)

    if (printTimer % 600 == 0):
      # print('Temperature is: ' + temperatureReading)
      # print('Humidity is: ' + humidityReading)
      # print('Air quality is: ' + airQualityReading)

      print('The heater relay is currently: ' + humidifierRelayStatusText)
      # print('The humidifier relay is currently: ' + humidifierRelayStatus)


    time.sleep(1)
    printTimer += 1

finally:
  printTimer = 0
  pins.cleanup()
