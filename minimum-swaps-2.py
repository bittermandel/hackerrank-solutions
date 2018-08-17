#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr, swaps=0):
    sorted_arr = sorted(arr)
    
    for ix, i in enumerate(arr, start=0):
        if i != sorted_arr[ix]:
            arr[i-1], arr[ix] = arr[ix], arr[i-1]
            swaps += 1

    if sorted(arr) == arr:
        return swaps
    else:
        return minimumSwaps(arr, swaps=swaps)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
