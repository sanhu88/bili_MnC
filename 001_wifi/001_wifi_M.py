import network
import time


def connect_wifi(wifi_ssid: str, wifi_key: str):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    time.sleep_ms(200)
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting to network...")
        wlan.connect(wifi_ssid, wifi_key)
        while not wlan.isconnected():
            time.sleep_ms(10)
    print("network config:", wlan.ifconfig())


if __name__ == "__main__":
    connect_wifi("disk0", "12345679")
