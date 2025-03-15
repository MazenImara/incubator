from machine import Pin, I2C
import sh1106
from settings import Settings

class Display:
    scalPin, sdaPin, resPin = 9, 8, 16
    oled = None
    pageNum = 0
    pageNums = 3
    settings = None

    def __init__(self, settings) -> None:
        i2c = I2C(0, scl=Pin(self.scalPin), sda=Pin(self.sdaPin), freq=400000)
        self.oled = sh1106.SH1106_I2C(128, 64, i2c, Pin(self.resPin), 0x3c, rotate=180)
        self.settings = settings
        self.page()

    def change(self):
        if self.pageNum < 3:
            self.pageNum +=1
        else:
            self.pageNum = 0
        self.page()

        

    def page(self):
        if self.pageNum == 1:
            self.page1()
        elif self.pageNum == 2:
            self.page2()
        elif self.pageNum == 3:
            self.page3()
        else:
            self.page0()

    def page0(self):
        self.oled.fill(0)
        self.oled.text('Temp: ' + str(self.settings['currentTemp']) + 'C', 0, 0, 1)
        self.oled.text('Hum: ' + str(self.settings['currentHum']) + '%', 0, 10, 1)
        self.oled.text('Settings', 35, 25, 1)
        self.oled.text('Temp: ' + str(self.settings['temp']) + 'C', 0, 35, 1)
        self.oled.text('Hum: ' + str(self.settings['hum']) + '%', 0, 45, 1)
        self.oled.text('Rotation: ' + str(self.settings['rotation']) + 'H', 0, 55, 1)
        self.oled.show()

    def page1(self):
        self.oled.fill(0)
        self.oled.text('Temperture', 20, 10, 1)
        self.oled.text(str(self.settings['temp']) + 'C', 45, 35, 1)
        self.oled.show()

    def page2(self):
        self.oled.fill(0)
        self.oled.text('Hummidity', 20, 10, 1)
        self.oled.text(str(self.settings['hum']) + '%', 45, 35, 1)
        self.oled.show()

    def page3(self):
        self.oled.fill(0)
        self.oled.text('Rotation', 20, 10, 1)
        self.oled.text(str(self.settings['rotation']) + 'H', 45, 35, 1)
        self.oled.show()