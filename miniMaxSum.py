#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#

def miniMaxSum(arr):
    arr.sort()   # O(n log(n)) complexity
    print(sum(arr) - arr[len(arr) - 1], sum(arr) - arr[0])
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
