import ujson as json

class Settings:
    fileName = 'settings.json'
    settings = None
    defaultSettings = {
        'temp': 37,
        'hum' : 50,
        'rotation': 1,
        'currentTemp': -1,
        'currentHum': -1
    }

    def __init__(self):
        self.checkDefaultSettings()

    def checkDefaultSettings(self):
        try:
            with open(self.fileName, 'r') as f:
                self.settings = json.load(f)
        except:
            self.saveDefaultSettings()

    def saveDefaultSettings(self):
        try:
            with open(self.fileName, 'w') as f:
                json.dump(self.defaultSettings, f)
        except:
                print("Error! Could not save default settings")

    def save(self):
        if self.settings == None:
             print("Settings is None")
             return
        try:
            with open(self.fileName, 'w') as f:
                json.dump(self.settings, f)
        except:
            print("Error! Could not save settings")

    def update(self, page, arrow):
        print(page)
        if page == 1:
            attr = 'temp'
        elif page == 2:
            attr = 'hum'
        elif page == 3:
            attr = 'rotation'
        else:
            return
        
        if arrow == 'up':
            self.settings[attr] +=1
        else:        
            if self.settings[attr] == 0:
                return
            self.settings[attr] -=1
        
        self.save()

    def updateCurrent(self, temp, hum):
        self.settings['currentTemp'] = temp
        self.settings['currentHum'] = hum        
            