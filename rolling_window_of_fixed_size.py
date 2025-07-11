#!/bin/python3

import math
import os
import random
import re
import sys

#
# The function is expected to return an INTEGER.
# The function accepts the following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # implement rolling window of fixed size
    count_of_matches = 0
    print("s:", s) 
    print("d:", d)
    print("m", m)
    for i in range(len(s) - m + 1):
        if sum(s[i: i + m]) == d:
            count_of_matches += 1
    return count_of_matches    


