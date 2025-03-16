# type: ignore
import urequests

class Action:
    setting = None
    display = None
    wifi = None
    def __init__(self, setting, dispaly, wifi) -> None:
        self.setting = setting
        self.display = dispaly
        self.wifi = wifi

    def callback(self, temp, hum):
        self.setting.updateCurrent(temp, hum)
        #self.checkTemp()
        #self.checkHum()
        self.updateServer()

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

    def updateServer(self):
        if self.wifi.connected:
            url = f"http://yallacloud.ddns.net/incubator/index.php?update&hum={self.setting.settings['currentHum']}&temp={self.setting.settings['currentTemp']}"

            try:
                response = urequests.get(url)
                print('Response status code:', response.status_code)
                print('Page content:', response.text)
            except Exception as e:
                print('Error visiting the page:', e)            
