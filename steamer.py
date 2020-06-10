import RPi.GPIO as GPIO
from time import sleep
import sys
import Adafruit_DHT


# GPIO.cleanup()
# The script as below using BCM GPIO 00..nn numbers

class sensor:
    def __init__(self, pin):
        self.pin = pin
        self.humidity = 0
        self.temperature = 0
    def getFreshHumidity(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 11, self.pin)
        return self.humidity

    def getFreshTemperature(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(11, self.pin)
        return self.temperature

    def getFreshData(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 11, self.pin)
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

# GPIO.setmode(GPIO.BCM)
# # Set relay pins as output
# GPIO.setup(fan1, GPIO.OUT)
# GPIO.setup(fan2, GPIO.OUT)
# GPIO.setup(fan_top, GPIO.OUT)
# GPIO.cleanup()
# print("all out")

# while (True):

#     # Turn all relays ON
#     GPIO.output(fan1, GPIO.HIGH)
#     GPIO.output(fan2, GPIO.HIGH)
#     GPIO.output(fan_top, GPIO.HIGH)
#     print("all high")
#     # Sleep for 5 seconds
#     sleep(5) 
#     # Turn all relays OFF
#     GPIO.output(18, GPIO.LOW)
#     GPIO.output(23, GPIO.LOW)
#     GPIO.output(24, GPIO.LOW)
#     GPIO.output(25, GPIO.LOW)
#     print("all low")
#     # Sleep for 5 seconds
#     sleep(5)

def main():
    # fan1 = fan(23)
    # fan2 = fan(24)
    # print(fan2.pin, fan1.pin)
    # fan2.on()
    # fan1.on()
    # sleep(5)
    # fan2.off()
    # sleep(2)
    # fan1.off()
    # sleep(5)
    # GPIO.cleanup()
    sensor1 = sensor(18)
    print(sensor1.getFreshHumidity)
    print(sensor1.getCachedTemperature)




if __name__ == "__main__":
    main()