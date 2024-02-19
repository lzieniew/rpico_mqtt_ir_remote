# Raspberry Pico W MQTT IR remote
Script for raspberry pi pico to send IR signals in reaction to MQTT messages

You will need to put umqtt library on rpi pico. You can do it by cloning https://github.com/micropython/micropython-lib and putting file micropython/umqtt.simple/umqtt/simple.py on the pico. It can be done with commands:
  - `sudo mpremote connect /dev/ttyACM0 mkdir :/lib/umqtt`
  - `sudo mpremote connect /dev/ttyACM0 cp micropython-lib/micropython/umqtt.simple/umqtt/simple.py :/lib/umqtt/simple.py`

upload to rpico with 
`sudo mpremote connect /dev/ttyACM0 cp main.py :/main.py`

You can also use this command to run the script immediately and see prints in terminal
`sudo mpremote connect /dev/ttyACM0 run main.py`

