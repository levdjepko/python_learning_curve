#!/bin/python3

import math
import os
import random
import re
import sys


'''
# Given a square matrix, calculate the absolute difference between its diagonals.
'''

def diagonalDifference(arr):
    firstDiagonal = secondDiagonal = 0    
    #print(arr)
    for i in range(len(arr)):
        firstDiagonal += arr[i][i]
        #print("First:", arr[i][i])
        secondDiagonal += arr[i][len(arr)- i - 1]
        #print("Second:", arr[i][len(arr)- i - 1])
    #print(firstDiagonal, secondDiagonal)    
    return abs(firstDiagonal - secondDiagonal)    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
