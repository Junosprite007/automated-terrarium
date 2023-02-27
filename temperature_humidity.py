import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

printTimer = 0
while True:
    humidity, temperatureC = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    temperatureF = temperatureC * (9 / 5) + 32

    if humidity is not None and temperatureC is not None:
        print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperatureC, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")
    time.sleep(1)
    printTimer += 1
