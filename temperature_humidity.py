import RPi.GPIO as GPIO
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

printTimer = 0
try:
  while True:
      humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

      if humidity is not None and temperature is not None:
          print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
      else:
          print("Failed to retrieve data from humidity sensor")
      time.sleep(1)
      printTimer += 1

finally:
  printTimer = 0
  GPIO.cleanup()

