#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    positive = negative = nulls = 0
    for i in range(len(arr)):
        # iterate over every item in the array and sort the numbers by the sign
        if arr[i] < 0:
            negative += 1
        elif arr[i] > 0:
            positive += 1
        else:
            nulls += 1
    print(format(positive/len(arr), '.6f'))
    print(format(negative/len(arr), '.6f'))
    print(format(nulls/len(arr), '.6f'))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
