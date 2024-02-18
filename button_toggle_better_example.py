from machine import Pin
import time

# Initialize pin 10 as an output and pin 5 as an input with a pull-up resistor.
led = Pin(10, Pin.OUT)
button = Pin(5, Pin.IN, Pin.PULL_UP)

led_state = False


def toggle_led():
    global led_state
    led_state = not led_state
    led.value(led_state)


def debounce(pin):
    time.sleep(0.01)
    return not pin.value()


# Main loop
while True:
    if not button.value() and debounce(button):
        toggle_led()
        while not button.value():
            time.sleep(0.01)
    time.sleep(0.01)  # Short delay to reduce CPU usage
