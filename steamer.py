import RPi.GPIO as GPIO
from time import sleep
import sys
import Adafruit_DHT
from pyHS100 import Discover
import logging
import atexit
import optparse
import sys
import time


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
        logging.info("init sensor: %s", self.pin)
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
        logging.info("init relay: %s", self.pin)
    def on(self):
        GPIO.output(self.pin , True) 
        logging.info("turning relay on: %s", self.pin)
    def off(self):
        GPIO.cleanup(self.pin)
        logging.info("turning relay off: %s", self.pin)
    def cleanup(self):
        logging.info("cleanup relay: %s", self.pin)
        GPIO.cleanup()

class powerPlug:
    def __init__(self):
        for dev in Discover.discover().values():
            plug = dev
        self.dev = plug
        logging.info("init power plug: %s", self.dev.model)
    def turn_on(self):
        self.dev.turn_on()
        logging.info("turning plug: %s ON", self.dev.model)
    def turn_off(self):
        self.dev.turn_off()
        logging.info("turning plug: %s OFF", self.dev.model)
    

def main():
    sensor1 = sensor(18)
    fan_top = fan(1)
    fan_inside = fan(2)
    plug = powerPlug()

    # plug.turn_on() # turned steamer on
    fan_inside.on() # turned fan inside on

    start_main_time = time.time()
    start_time = time.time()
    steam_time = 300
    steam_elapsed_time = time.time() - start_main_time # diff of steam time
    while steam_elapsed_time < steam_time:
        while sensor1.getFreshHumidity() < 90:
            plug.turn_on() # turned steamer on
            sleep(10)

            elapsed_time = time.time() - start_time
            if elapsed_time > steam_time:
                logging.info("Finished iterating in: %s", elapsed_time)
                break
        plug.turn_off()
        sleep(2)
        steam_elapsed_time = time.time() - start_main_time # diff of steam time

    


    # logging.info("hum: %s", sensor1.getFreshHumidity())
    # logging.info("temp: %s", sensor1.getCachedTemperature())

    # p = powerPlug()
    # logging.info("dev is on: %s", p.dev.is_on)
    # logging.info("dev is off: %s", p.dev.is_off)




if __name__ == "__main__":
    main()