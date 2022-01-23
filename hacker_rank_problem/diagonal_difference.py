

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    d1 = []
    d2 = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i == j:
                d1.append(arr[i][j])
                if len(arr) // 2 == i:
                    d2.append(arr[i][j])
                
            elif (j == (len(arr) - i - 1)):
                d2.append(arr[i][j])
                
    sum_1 = sum(d1)
    sum_2 = sum(d2)
    return abs(sum_1 - sum_2)



if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)

   
