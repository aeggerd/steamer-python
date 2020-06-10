import RPi.GPIO as GPIO
from time import sleep
import sys
import Adafruit_DHT
from pyHS100 import Discover
import logging
import atexit
import optparse
import sys


FORMAT = "%(asctime)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)


def onexit():
    GPIO.setwarnings(False)
    GPIO.cleanup()
    logging.info("shutting down gracefully")

atexit.register(onexit)

# parser = optparse.OptionParser()
# parser.add_option('-q', '--query',
#     action="store", dest="query",
#     help="query string", default="spam")

# options, args = parser.parse_args()
# print(args.query)



class sensor:
    def __init__(self, pin):
        self.pin = pin
        self.humidity = 0
        self.temperature = 0
    def getFreshHumidity(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, self.pin)
        return self.humidity

    def getFreshTemperature(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, self.pin)
        return self.temperature

    def getFreshData(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, self.pin)
        return self.humidity, self.temperature
    
    def getCachedData(self):
        return self.humidity, self.temperature

    def getCachedHumidity(self):
        return self.humidity

    def getCachedTemperature(self):
        return self.temperature

GPIO.setmode(GPIO.BCM)
class fan:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
    def on(self):
        # GPIO.output(self.pin, GPIO.HIGH)
        GPIO.output(self.pin , True) 
        print("on: ", self.pin)
    def off(self):
        print("off: ", self.pin)
        # GPIO.output(self.pin , False)
        GPIO.cleanup(self.pin)
        # GPIO.output(self.pin, GPIO.LOW)
    def cleanup(self):
        GPIO.cleanup()

class powerPlug:
    def __init__(self):
        for dev in Discover.discover().values():
            plug = dev
        self.dev = plug

def main():
    sensor1 = sensor(18)
    logging.info("hum: %s", sensor1.getFreshHumidity())
    logging.info("temp: %s", sensor1.getCachedTemperature())

    p = powerPlug()
    logging.info("dev is on: %s", p.dev.is_on)
    logging.info("dev is off: %s", p.dev.is_off)




if __name__ == "__main__":
    main()