
import math
import os
import random
import re
import sys

def timeConversion(s): 

    if s[-2:] == 'PM' and s[:2] != '12':
        time = s.strip('PM')
        conv_time = str(int(time[:2])+12)+time[2:]

    elif s[-2:] == 'PM' and s[:2] == '12':
        conv_time = s.strip('PM')

    elif s[-2:] == 'AM' and s[:2] == '12':
        time = s.strip('AM')
        conv_time = '0'+str(int(time[:2])-12)+time[2:]

    else:
        conv_time = s.strip('AM')
        
    return conv_time

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)

    
