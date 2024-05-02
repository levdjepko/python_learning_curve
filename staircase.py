#!/bin/python3
'''Staircase detail

This is a staircase of size :

   #
  ##
 ###
#### '''
import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    line = ' '*n
    for i in range(n):
        line = line[0:n-i-1] + "#" + line[n-i:]
        print(line)   

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
