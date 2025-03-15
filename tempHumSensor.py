import dht
from machine import Pin

class Sensor:
    sensor = None
    action = None
    def __init__(self, action) -> None:
        self.action = action
        self.sensor = dht.DHT11(Pin(19))
    

    def measure(self):
        self.sensor.measure()
        self.action.callback(self.sensor.temperature(), self.sensor.humidity())