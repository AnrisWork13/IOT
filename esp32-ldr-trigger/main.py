# ESP32 DevKit LDR Trigger (MicroPython)
import network
import urequests
from machine import Pin
import time

ldr = Pin(13, Pin.IN)

ssid = 'YOUR_SSID'
password = 'YOUR_PASSWORD'
cam_ip = '192.168.1.100'  # Replace with ESP32-CAM IP

# Connect to Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    pass
print("Connected to WiFi:", wifi.ifconfig())

while True:
    if ldr.value() == 1:
        print("Light detected — triggering ESP32-CAM...")
        try:
            urequests.get(f"http://{cam_ip}/capture")
        except:
            print("Failed to contact camera")
        time.sleep(10)
    else:
        print("Too dark.")
        time.sleep(5)

