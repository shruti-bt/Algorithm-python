
import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    
    result = 0
    for i in range(len(ar)):
        result = result + ar[i]
    return result
        
if __name__ == '__main__':

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    print(result)
