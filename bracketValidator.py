#!/bin/python3

import math
import os
import random
import re
import sys


def isBalanced(s):
    
    # Write your code here
    # for i in range(0, len(s)//2):
    #     if (s[i] == '(' and s[len(s)-1-i] == ')') or (s[i] == '[' and s[len(s)-1-i] == ']') or (s[i] == '{' and s[len(s)-1-i] == '}'):
    #         continue
    #     else:
    #         return 'NO'
    # stuff above doesn't work because the secription of the problem is flawed.
    # we might want to just add items to the array as we go, and pop them as we see the matching parenthesis
    brackets = []
    
    if (len(s)) == 1:
        return 'NO'
    
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[' :  # add the opening brackets, endlessly
            #print("Add", s[i])
            
            brackets.append(s[i])
        elif s[i] not in ('(', '{', '['):   # we have to match here
           
            # Item not in "append" list
            if (len(brackets) > 0):
                #print("remove", s[i])
                item = brackets.pop() 
                if (item == '{' and s[i] != '}') or (item == '(' and s[i] != ')') or (item == '[' and s[i] != ']'):
                    return 'NO'
            else:
                return 'NO'        
    if len(brackets) > 0:
        return 'NO'            
    return 'YES'           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
