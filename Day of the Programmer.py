#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    ye = 31+28+31+30+31+30+31+31
    leapye = 31+29+31+30+31+30+31+31
    m0 = 0
    m = 9
    if 1700<=year<1918:
        if year%4 !=0:
            day = 256 - ye
        elif year%4 == 0:
            day = 256 - leapye
    elif year == 1918:
        day = 256 - (31+15+31+30+31+30+31+31)
    elif 1919<=year<=2700:
        if year%400 == 0 or (year%4==0 and year%100!=0):
            day = 256-leapye
        else:
            day = 256-ye
    date = str(day)+'.'+str(m0)+str(m)+'.'+str(year)
    return date

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
