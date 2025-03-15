from machine import Pin
from settings import Settings
from display import Display
import utime
from tempHumSensor import Sensor
from action import Action
from rotation import Rotation

setting = Settings()
display = Display(setting.settings)
action = Action(setting, display)
sensor = Sensor(action)
rotation = Rotation(setting.settings)


btnDown = Pin(16, Pin.IN, Pin.PULL_UP)
btnUp = Pin(17, Pin.IN, Pin.PULL_UP)
btnChange = Pin(18, Pin.IN, Pin.PULL_UP)

sensorTimer = 0
testRotate = 0
while True:
    utime.sleep(0.1)
    sensorTimer += 0.1

    rotation.check()    

    if testRotate > 0 and sensorTimer > 2:
        print("*************")
        rotation.rotate()
        testRotate -=1
    
    if sensorTimer > 2 and display.pageNum == 0:
        sensor.measure()
        display.page0()
        sensorTimer = 0

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
        testRotate = 5



