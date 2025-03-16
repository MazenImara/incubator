from machine import Pin
from settings import Settings
from display import Display
import utime
from tempHumSensor import Sensor
from action import Action
from rotation import Rotation
from wifi import Wifi

setting = Settings()
display = Display(setting.settings)
wifi=Wifi()
action = Action(setting, display, wifi)
sensor = Sensor(action)
rotation = Rotation(setting.settings)


btnDown = Pin(16, Pin.IN, Pin.PULL_UP)
btnUp = Pin(17, Pin.IN, Pin.PULL_UP)
btnChange = Pin(18, Pin.IN, Pin.PULL_UP)

sensorTimer = 0
rotateCoun = 0
wifiTimer=0
while True:
    utime.sleep(0.1)
    sensorTimer += 0.1
    wifiTimer += 0.1

    rotation.check()

    if rotateCoun > 0 and sensorTimer > 2:
        print("*************")
        rotation.rotate()
        rotateCoun -=1
    
    if sensorTimer > 2 and display.pageNum == 0:
        sensor.measure()
        display.page0()
        sensorTimer = 0

    if not wifi.connected() and wifiTimer > 1:
        wifi.connect()
        wifiTimer = 0

    if btnChange.value() == 0:
        print("Change")
        display.change()

    if btnUp.value() == 0:
        print("Up")
        setting.update(display.pageNum, 'up')
        display.page()

    if btnDown.value() == 0:
        print("Down")
        setting.update(display.pageNum, 'down')
        display.page()

    if btnUp.value() == 0 and btnDown.value() == 0:
        rotateCoun = 5



