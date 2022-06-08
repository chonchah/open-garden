import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


def writeGPIO(pin, state):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, state)

