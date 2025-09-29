import math
import os
import random
import re
import sys

def closestNumbers(arr):
    arr.sort()
    # assume the first difference to be the smallest one, then iterate over the array
    smallest_diff = arr[1] - arr[0]
    new_array = []
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] < smallest_diff:
            smallest_diff = arr[i + 1] - arr[i]
            new_array.clear()
        if arr[i + 1] - arr[i] == smallest_diff:
            new_array.append(arr[i])
            new_array.append(arr[i + 1])
    return new_array        
