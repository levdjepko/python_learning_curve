#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#


def birthdayCakeCandles(candles):
    # Write your code here
    candles.sort(reverse=True)
    count_of_tallest = 0
    tallest_item = candles[0]
    for i in range(len(candles)):
        # count, how many "tallest" candles there are. Shortcut once another size is encountered
        if candles[i] == tallest_item:
            count_of_tallest += 1
        else:
             break
    return count_of_tallest         
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
