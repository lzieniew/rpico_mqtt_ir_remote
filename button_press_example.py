from machine import Pin
import time

# Configure pin 5 as input with an internal pull-up resistor
button = Pin(5, Pin.IN, Pin.PULL_UP)

# Configure pin 10 as output
led = Pin(10, Pin.OUT)

while True:
    # Check if button is pressed (the value will be low due to pull-up resistor)
    if button.value() == 0:
        led.on()  # Turn the LED (or other device on pin 10) on
        print("Button pressed, pin 10 is HIGH")
    else:
        led.off()  # Turn the LED (or other device on pin 10) off
        print("Button not pressed, pin 10 is LOW")

    # Small delay to debounce the button and reduce CPU usage
    time.sleep(0.1)
