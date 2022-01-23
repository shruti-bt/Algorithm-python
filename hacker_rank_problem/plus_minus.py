#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i == 0:
            zero += 1
        elif i < 0:
            neg += 1
            
    print(
        round(pos/len(arr), 6), 
        round(neg/len(arr), 6), 
        round(zero/len(arr), 6), 
        sep='\n'
    )
            
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
