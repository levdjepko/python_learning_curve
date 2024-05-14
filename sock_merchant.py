#!/bin/python3

import math
import os
import random
import re
import sys



def sockMerchant(n, ar):
    # find the number of pairs in the array
    ar.sort()
    total_count = 0
    # try to loop through the sorted array just once
    for i in range(len(ar) - 1):
        if i is not -1:    # to skip the next item as we already accounted for it
            if ar[i] == ar[i + 1]:  # found a pair
                total_count += 1
                ar[i+1] = -1            
    return total_count
    
      
