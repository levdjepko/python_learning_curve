#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def getSumOfDigits(num: int)->int:
    # this function sums all the numbers in any integer
    # for example, 1234 = > 1 + 2 + 3 + 4 = 10
    number_as_string = str(num)
    super_digit = 0
    for i in range(len(number_as_string)):
        super_digit += int(number_as_string[i])
    return super_digit    


def superDigit(n, k):
    # recursively, count the sum of all the numbers in an integer
    n = getSumOfDigits(n) * k
    if n < 10:
        return n
    else:
        while n >= 10:
            n = getSumOfDigits(n)
    return n
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
