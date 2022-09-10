from machine import Pin  # type: ignore
from time import sleep

pin = Pin(25, Pin.OUT)

while True:
    pin.toggle()
    sleep(1)