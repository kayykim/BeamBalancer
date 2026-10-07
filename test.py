import serial
import time
from threading import Thread

PORT = "/dev/tty.usbmodem1401"

def servo_thread():
    print("Thread started")

    servo = serial.Serial(PORT, 9600)
    time.sleep(2)

    print("Sending 5")
    servo.write(bytes([5]))
    time.sleep(2)

    print("Sending 15")
    servo.write(bytes([15]))
    time.sleep(2)

    print("Sending 25")
    servo.write(bytes([25]))
    time.sleep(2)

    servo.close()
    print("Thread finished")


thread = Thread(target=servo_thread)
thread.start()

# IMPORTANT: wait for thread to finish
thread.join()

print("Program finished")