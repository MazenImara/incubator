# type: ignore
import network

class Wifi:
    # Wi-Fi credentials
    SSID = 'Mazen'         # Replace with your Wi-Fi SSID
    PASSWORD = '+-5m12345' # Replace with your Wi-Fi password
    wlan = None

    def __init__(self) -> None:
        self.wlan = network.WLAN(network.STA_IF)  # Station (Client) mode
        self.wlan.active(True)  # Enable the Wi-Fi interface

    def connect(self):
        if not self.connected():
            print('Connecting to network...')
            self.wlan.connect(self.SSID, self.PASSWORD)
            print('Connected to Wi-Fi')
            print('IP address:', self.wlan.ifconfig()[0])
            
    def connected(self):
        return self.wlan.isconnected()