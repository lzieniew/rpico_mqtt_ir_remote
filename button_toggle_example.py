from machine import Pin
import time

# Initialize pin 10 as an output pin
led = Pin(10, Pin.OUT)
# Initialize pin 5 as an input pin with an internal pull-up resistor
button = Pin(5, Pin.IN, Pin.PULL_UP)

# Variable to store the LED state
led_state = False


# Function to toggle the LED state
def toggle_led():
    global led_state
    led_state = not led_state
    led.value(led_state)
    print("LED Toggled: ", "ON" if led_state else "OFF")


print("Program started. Press the button to toggle the LED.")

# Main loop
while True:
    # Check if the button is pressed (the logic is inverted due to the pull-up resistor)
    if not button.value():
        toggle_led()
        # Debounce delay to avoid multiple toggles from a single press
        time.sleep(0.5)
    else:
        # Print the waiting message every second when the button is not pressed
        print("Waiting for button press...")
        time.sleep(1)
