
# BMP180 and reapberry pi pico

## BMP Module


## Pin Connection
| raspberry pi pico w | | BMP180 Module|
| :--- | :---: |---: |
| VBUS | -> | VCC |
| Gnd | -> | GND |
| GP16 | -> | SDA |
| GP17 | -> | SCL |
## Installing
This project adopts MicroPython as the programming language, hence we have to setup the MicroPython on the raspberry pi pico. At raspberry pi's official webside [here](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html), we can find the explain of setup in detail.

## Thonny
We use Thonny as development enviroment which can be downloaded at [here](https://thonny.org/)

## Code
Save the code as main.py and bmp.py files into the raspberry pi pico.

## Reference
* Raspberry Pi Pico <br>
https://www.raspberrypi.com/products/raspberry-pi-pico/
* BMP180 data sheet<br>
https://www.mouser.tw/datasheet/2/783/BST-BMP180-DS000-1509579.pdf
* MicroPython i2c<br>
https://docs.micropython.org/en/latest/library/machine.I2C.html

## license
Licensed under creative commons attribution CC BY-NC-SA
