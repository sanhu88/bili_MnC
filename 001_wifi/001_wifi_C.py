import wifi
import time


def connect_wifi(wifi_ssid: str, wifi_key: str):
    wlan = wifi.radio
    wlan.enabled = False
    time.sleep(0.2)
    wlan.enabled = True
    if not wlan.connected:
        print("connecting to network...")
        wlan.connect(wifi_ssid, wifi_key)
        while not wlan.connected:
            time.sleep(0.01)
    print("network config:", wlan.ipv4_address)


if __name__ == "__main__":
    connect_wifi("disk0", "12345679")
