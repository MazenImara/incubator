from machine import Pin
import stepper
from time import sleep

class Rotation:
    motor = None
    relay = None
    settings = None
    timer = 0

    def __init__(self, settings) -> None:
        self.motor = stepper.HalfStepMotor.frompins(26, 22, 21, 20)
        self.motor.reset()
        self.relay = Pin(27, Pin.OUT)
        self.relay.low()
        self.settings = settings

    def check(self):
        if self.settings['rotation'] < 1:
            return

        self.timer += 0.1

        if self.timer > self.settings['rotation'] * 3600:
            print('rotate' + str(self.settings['rotation']))
            self.rotate()
            self.timer = 0

    def rotate(self):
        self.relay.high()
        self.motor.step(750)
        self.relay.low()
