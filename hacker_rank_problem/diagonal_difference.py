

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    d1 = 0
    d2 = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == j:
                d1 += arr[i][j]
                
            if (i + j) == (len(arr) - 1):
                d2 += arr[i][j]
                
    return abs(d1 - d2)


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)

   
