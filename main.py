# n = 700
# m = 1400
# output = (m - 1 ) // n + 1
# print(output)

import modul1

print(modul1.max1(5, 3))
#######
from modul1 import max1 

print(max1(10, 9))
#######
from modul1 import *

print(max1(10,8))
#######
import modul1 as m1

print(m1.max1(7,6))