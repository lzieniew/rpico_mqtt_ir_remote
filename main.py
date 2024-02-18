import machine
import utime
import network
from umqtt.simple import MQTTClient

# WiFi details
ssid = "doskozza"
password = "osiemznakow"

# MQTT details
mqtt_server = "ejaj.local"
# If you're using a specific port for MQTT (default is 1883), include it here
mqtt_port = 1883


# Connect to WiFi
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    # Wait for connection
    while not wlan.isconnected():
        pass

    print("Connected to WiFi")


# Callback function to handle received messages
def on_message(topic, msg):
    print("Received message:", topic, msg)
    if msg == b"Power Stereo":
        pin_15.toggle()


# Set up pin 15 for MQTT message toggle
pin_15 = machine.Pin("LED", machine.Pin.OUT)

# Connect to WiFi
connect_to_wifi()

# Set up MQTT client
client = MQTTClient("pico_w_client", mqtt_server, port=mqtt_port)
client.set_callback(on_message)
client.connect()
client.subscribe("test/topic")

print("Connected to MQTT broker, subscribed to topic")

# Main loop
try:
    while True:
        client.wait_msg()  # Wait for messages, this is a blocking call
except KeyboardInterrupt:
    client.disconnect()
