#!/bin/python3

import math
import os
import random
import re
import sys


#  Given an array of integers, where all elements but one occur twice, find the unique element.

def lonelyinteger(a):    
    # we can iterate over this array with a hashset or hashmap
    # to effectively keep track of all the keys, and the number of the element' occurences
    
    hashMap={}
    index=-1
    for i in range(len(a)):
        if a[i] not in hashMap:
            hashMap[a[i]]=1  # add this element to the hashMap as a key, and it occured 1 time            
        else:
            hashMap[a[i]]=2    
    #print(hashMap)               
    for key, value in hashMap.items():
        #print (key, value)
        if value == 1:
            return key         
    return 0            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
