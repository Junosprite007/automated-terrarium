import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Set pins
heaterRelayPin = 21
heaterRelayStatus = GPIO.LOW
heaterRelayStatusText = "LOW"

# Set important limits
minTemp = 76     # in Fahrenheit
maxTemp = 79     # in Fahrenheit
minHumidity = 90     # in percentage
maxHumidity = 95     # in percentage

# How often do you want to record data to the backend (in seconds)?
# every 5 minutes, though, currently this does not necessarily correspond to 5 minutes.
dataRecordingInterval = 600

# Relay
GPIO.setup(heaterRelayPin, GPIO.OUT)
GPIO.output(heaterRelayPin, heaterRelayStatus)

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
    #   heaterRelayStatus = GPIO.HIGH
    #   GPIO.output(heaterRelayPin, heaterRelayStatus)
    # elif (temperatureReading >= maxTemp - 1):
    #   # Turn on the heater by activating the relay
    #   heaterRelayStatus = GPIO.LOW
    #   GPIO.output(heaterRelayPin, heaterRelayStatus)
    
    # # Handle the humidifier relay.
    # if (humidityReading < minHumidity):
    #   # Turn on the heater by activating the relay
    #   heaterRelayStatus = GPIO.HIGH
    #   GPIO.output(heaterRelayPin, heaterRelayStatus)
    # elif (humidityReading >= maxHumidity - 1):
    #   # Turn on the heater by activating the relay
    #   heaterRelayStatus = GPIO.LOW
    #   GPIO.output(heaterRelayPin, heaterRelayStatus)

    # if (printTimer % 600 == 0):
      # print('Temperature is: ' + temperatureReading)
      # print('Humidity is: ' + humidityReading)
      # print('Air quality is: ' + airQualityReading)

      # print('The heater relay is currently: ' + heaterRelayStatusText)
      # print('The humidifier relay is currently: ' + humidifierRelayStatus)

    print('The heater relay is currently: ' + heaterRelayStatusText)
    heaterRelayStatus = GPIO.HIGH
    GPIO.output(heaterRelayPin, heaterRelayStatus)
    heaterRelayStatusText = "HIGH"
    time.sleep(1)
    printTimer += 1
    
    print('The heater relay is currently: ' + heaterRelayStatusText)
    heaterRelayStatus = GPIO.LOW
    GPIO.output(heaterRelayPin, heaterRelayStatus)
    heaterRelayStatusText = "LOW"
    time.sleep(1)
    printTimer += 1

finally:
  printTimer = 0
  GPIO.cleanup()
