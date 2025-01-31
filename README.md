
# BMP180 and reapberry pi pico

## BMP Module
<br>
<br>

## Pin Connection
| raspberry pi pico w | | BMP180 Module|
| :--- | :---: |---: |
| VBUS | -> | VCC |
| Gnd | -> | GND |
| GP16 | -> | SDA |
| GP17 | -> | SCL |
<br>

## Installing
This project adopts MicroPython as the programming language, hence we have to setup the MicroPython on the raspberry pi pico. At raspberry pi's official webside [here](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html), we can find the explain of setup in detail.
<br>
<br>

## Thonny
We use Thonny as development enviroment which can be downloaded at [here](https://thonny.org/)
<br>
<br>

## Quick Start
Save the code as main.py and bmp.py files into the raspberry pi pico.
<br>
<br>

## Class BMP
### Constructor
    class bmp.BMP( [i2c_addr = __BMP180_ADDR],
                   [i2c_id = 0],
                   [scl_pin = 17],
                   [sda_pin = 16] )

Construct a new BMP object and initintalize the BMP180 sensor with the given arguments:
* __i2c_addr__ The i2c address of the BMP180 (optional)
* __i2c_id__ The i2c ID of the pi pico (optional)
* __scl_pin__ The pin of the scl (optional)
* __sda_pin__ The pin of the sda (optional)
<br>
<br>

### Method

    class bmp.get_temp()

Acquire the measurement value of temperature.

    class bmp.get_pressure()

Acquire the measurement value of pressure.

<br><br>

## Reference
* Raspberry Pi Pico <br>
https://www.raspberrypi.com/products/raspberry-pi-pico/
* BMP180 data sheet<br>
https://www.mouser.tw/datasheet/2/783/BST-BMP180-DS000-1509579.pdf
* MicroPython i2c<br>
https://docs.micropython.org/en/latest/library/machine.I2C.html
<br><br>

## license
Licensed under creative commons attribution CC BY-NC-SA
