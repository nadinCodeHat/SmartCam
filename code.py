import RPi.GPIO as GPIO
import time

sensor1 = 17
sensor2 = 27
sensor3 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor1, GPIO.IN)
GPIO.setup(sensor2, GPIO.IN)
GPIO.setup(sensor3, GPIO.IN)

GPIO.setup(14, GPIO.OUT)
motor = GPIO.PWM(14, 50)
motor.start(7.5)


def function1(sensor1):
    if GPIO.input(sensor1):
        print("Sound Detected by sensor1!")
        motor.ChangeDutyCycle(7.5)
        time.sleep(1)


def function2(sensor2):
    if GPIO.input(sensor2):
        print("Sound Detected by sensor2!")
        motor.ChangeDutyCycle(2.5)
        time.sleep(1)


def function3(sensor3):
    if GPIO.input(sensor3):
        print("Sound Detected by sensor3!")
        motor.ChangeDutyCycle(12.5)
        time.sleep(1)


GPIO.add_event_detect(sensor1, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(sensor1, function1)

GPIO.add_event_detect(sensor2, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(sensor2, function2)

GPIO.add_event_detect(sensor3, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(sensor3, function3)

while True:
    time.sleep(1)
