import RPi.GPIO as GPIO
import dht11
import time
import urllib.request

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using gpio 3
instance = dht11.DHT11(pin = 3)

myurl = "https://api.thingspeak.com/update?api_key=OADL5DKOWI3JC7WQ&field"
switch = 1
while True:
    result = instance.read()

    if result.is_valid():
        try:
            if switch == 1:
                print("Temperature: %d C" % result.temperature)
                url1 = myurl + "1="+ str(result.temperature)
                f1 = urllib.request.urlopen(url1)
                print(str(f1.read()))
                switch = 2
            elif switch == 2:
                print("Humidity: %d %%" % result.humidity)
                url2 = myurl + "3=" + str(result.humidity)
                f2 = urllib.request.urlopen(url2)
                print(str(f2.read()))
                switch = 1
        except urllib.error.URLError as e:
            print(e)
            time.sleep(5)
        time.sleep(15)
    else:
        print("Error: %d" % result.error_code)
    time.sleep(1)
