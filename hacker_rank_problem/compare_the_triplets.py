import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    count_a = 0
    count_b = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            count_a += 1
        elif a[i] == b[i]:
            pass
        elif a[i] < b[i]:
            count_b += 1
    return count_a, count_b
    
if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)
