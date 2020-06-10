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
        self.humidity, self.temperature = Adafruit_DHT.read_retry(11, self.pin)
        return self.humidity

    def getFreshTemperature(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(11, self.pin)
        return self.temperature

    def getFreshData(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(11, self.pin)
        return self.humidity, self.temperature
    
    def getCachedData(self):
        return self.humidity, self.temperature

    def getCachedHumidity(self):
        return self.humidity

    def getCachedTemperature(self):
        return self.temperature

class fan:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
    def on(self):
        print(self.pin)
        GPIO.output(self.pin, GPIO.HIGH)
    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

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
    fan1 = fan(17)
    print(fan1.pin)
    fan2 = fan(18)
    print(fan2.pin)
    fan_top = fan(27)
    print(fan_top.pin)

    GPIO.cleanup()




if __name__ == "__main__":
    main()