import RPi.GPIO as GPIO
import time

# use BCM numbering
GPIO.setmode(GPIO.BCM)

# pins you chose
led_pins = [17, 27, 22]

# setup pins as outputs
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        for pin in led_pins:
            GPIO.output(pin, GPIO.HIGH)  # led on
            time.sleep(0.5)
            GPIO.output(pin, GPIO.LOW)   # led off
except KeyboardInterrupt:
    GPIO.cleanup()
