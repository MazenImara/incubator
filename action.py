

class Action:
    setting = None
    display = None
    def __init__(self, setting, dispaly) -> None:
        self.setting = setting
        self.display = dispaly

    def callback(self, temp, hum):
        self.setting.updateCurrent(temp, hum)
        self.checkTemp()
        self.checkHum()

    def checkTemp(self):
        if self.setting.settings['currentTemp'] > self.setting.settings['temp']:
            print("Temp is bigger")      
        elif self.setting.settings['currentTemp'] < self.setting.settings['temp']:
            print("Temp is smaller")
        else:
            print("Temp is ok")

    def checkHum(self):
        if self.setting.settings['currentHum'] > self.setting.settings['hum']:
            print("Hum is bigger")      
        elif self.setting.settings['currentHum'] < self.setting.settings['hum']:
            print("Hum is smaller")
        else:
            print("Hum is ok")