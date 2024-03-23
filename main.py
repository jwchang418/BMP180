import bmp

b = bmp.BMP()
t = b.get_temp()
print('temp = {} °C'.format(t/10))
p = b.get_pressure()
print('pressure = {} pa'.format(p))
