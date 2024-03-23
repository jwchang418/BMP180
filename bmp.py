# bmp.py
# Copyright (c) 2024 by Jun-Wei Chang.
# All rights reserved.
# Released under creative commons attribution CC BY-NC-SA.

import machine
import ustruct
import time

class BMP():
    # APDS-9151's I2C address
    __BMP180_ADDR = 0x77

    # Registers
    __Calibr_Coeff_ADDR = 0xAA
    __B5 = None
    __OSS = 0

    def __init__(self, i2c_addr = __BMP180_ADDR, i2c_id = 0, scl_pin = 17, sda_pin = 16):
        # Set i2c pins and initialize
        self.i2c = machine.I2C(i2c_id, scl=machine.Pin(scl_pin), sda=machine.Pin(sda_pin))
        self.i2c_addr = i2c_addr
        self.init_bmp()
        return None


    # read data from register
    def __read_reg(self,reg_addr,data_len):
        return self.i2c.readfrom_mem( self.i2c_addr, reg_addr, data_len )


    # write data to register
    def __write_reg(self,reg_addr,set_data):
        self.i2c.writeto_mem( self.i2c_addr, reg_addr, set_data)
        return True
    

    def init_bmp(self):
        self.__get_calibr_coeff()
        return True


    def set_oss(self,oss):
        self.__OSS = oss
        return True
    

    def __get_calibr_coeff(self):
        data_bytes = self.__read_reg(self.__Calibr_Coeff_ADDR,22)
        self.__AC1 = ustruct.unpack_from(">h",data_bytes,0)[0]
        self.__AC2 = ustruct.unpack_from(">h",data_bytes,2)[0]
        self.__AC3 = ustruct.unpack_from(">h",data_bytes,4)[0]
        self.__AC4 = ustruct.unpack_from(">H",data_bytes,6)[0]
        self.__AC5 = ustruct.unpack_from(">H",data_bytes,8)[0]
        self.__AC6 = ustruct.unpack_from(">H",data_bytes,10)[0]
        self.__B1 = ustruct.unpack_from(">h",data_bytes,12)[0]
        self.__B2 = ustruct.unpack_from(">h",data_bytes,14)[0]
        self.__MB = ustruct.unpack_from(">h",data_bytes,16)[0]
        self.__MC = ustruct.unpack_from(">h",data_bytes,18)[0]
        self.__MD = ustruct.unpack_from(">h",data_bytes,20)[0]
        return True


    def get_UT(self):
        self.__write_reg(0xF4,bytes([0x2E]))
        time.sleep(0.1)
        data_bytes = self.__read_reg(0xF6,2)
        return ustruct.unpack(">h",data_bytes)[0]


    def get_CT(self):
        t = (self.__B5+8)//16
        return t
    

    def get_param_B5(self,UT):
        X1 = (UT-self.__AC6)*self.__AC5//32768
        X2 = self.__MC*2048//(X1+self.__MD)
        self.__B5 = X1 + X2
        return True


    def get_temp(self):
        ut = self.get_UT()
        self.get_param_B5(ut)
        t = self.get_CT()
        return t


    def get_pressure(self):
        if(self.__B5):
            up = self.get_UP()
            p = self.get_CP(up)
            return p
        else:
            print("ERROR:your need the B5")


    def get_UP(self):
        self.__write_reg(0xF4,bytes([0x34+(self.__OSS<<6)]))
        time.sleep(0.1)
        data_bytes = self.__read_reg(0xF6,3)
        UP = ustruct.unpack(">i",b'\x00' + data_bytes)[0]
        UP = UP >> (8-self.__OSS)
        return UP


    def get_CP(self,UP):
        B6 = self.__B5-4000
        X1 = (self.__B2 * (B6*B6/(pow(2,12))))/(pow(2,11))
        X2 = self.__AC2*B6/(pow(2,11))
        X3 = X1+X2
        B3 = ((self.__AC1*4+X3)*pow(2,self.__OSS)+2)/4
        X1 = self.__AC3*B6/pow(2,13)
        X2 = (self.__B1 * (B6*B6/(pow(2,12))))/(pow(2,16))
        X3 = ((X1+X2)+2)/pow(2,2)
        B4 = self.__AC4*int(X3+32768)/(pow(2,15))
        B7 = (UP-B3)*(50000>>self.__OSS)

        p = (B7*2)/B4

        X1 = (p/pow(2,8))*(p/pow(2,8))
        X1 = (X1*3038)/pow(2,16)
        X2 = (-7357*p)/pow(2,16)
        p = p+(X1+X2+3791)/pow(2,4)
        return p