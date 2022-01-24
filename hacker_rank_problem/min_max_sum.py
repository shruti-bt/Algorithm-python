

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    # Write your code here
    result = []
    for i in range(len(arr)):
        new_arr = arr.copy()
        new_arr.pop(i)
        sum_ = sum(new_arr)
        result.append(sum_)
    
    Max = max(result)
    Min = min(result)
    print(Min, Max)
               
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
