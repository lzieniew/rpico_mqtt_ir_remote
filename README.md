# rpico_mqtt_ir_remote
Script for raspberry pi pico to send IR signals in reaction to MQTT messages

You will need to put umqtt library on rpi pico. You can do it by cloning https://github.com/micropython/micropython-lib and putting file micropython/umqtt.simple/umqtt/simple.py on the pico. It can be done with command
`sudo ampy --port /dev/ttyACM0 put micropython-lib/micropython/umqtt.simple/umqtt/simple.py /lib/umqtt/simple.py`
I order to do this there has to be /lib/umqtt directory on raspberry pico. You can create it with rshell:
- `sudo rshell -p /dev/ttyACM0`
- then go `cd /pyboard`
- `mkdir lib/umqtt`

upload to rpico with 
`sudo ampy -p /dev/ttyACM0 put main.py`

