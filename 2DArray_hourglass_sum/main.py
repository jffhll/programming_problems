#!/bin/python3

import math
import os
import random
import re
import sys

# From: https://www.hackerrank.com/challenges/2d-array/problem
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    max = -10
    for i in range(4): # we can assume '4' because it's guaranteed to be a 6x6
        for j in range(4):
            sum = calcHour(arr, i, j)
            #print(str(sum), end=",")
            if sum > max:
                max = sum
        #print()
    return max

def calcHour(arr, x_offset, y_offset):
    x_start_index = x_offset
    y_start_index = y_offset
    
    hourglass_total = 0
    #add up the top row
    for i in range(3):
        hourglass_total += arr[x_start_index][y_start_index + i]
    
    hourglass_total += arr[x_start_index+1][y_start_index+1]
    
    #add up the bottom row
    for i in range(3):
        hourglass_total += arr[x_start_index+2][y_start_index +i]
        
    return hourglass_total
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()